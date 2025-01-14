FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

COPY script/ /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import yaml; config = yaml.safe_load(open('/app/config.yaml')); \
    [print(f'export {key.upper()}=\"{value}\"') for key, value in config.items()]" > /app/env.sh

RUN chmod +x /app/env.sh

# Create log directory and set permissions
RUN mkdir -p /var/log/access_verifier && chown -R appuser:appgroup /var/log/access_verifier

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["/bin/sh", "-c", ". /app/env.sh && gunicorn -w 4 -b 0.0.0.0:5000 AccessVerifier:app"]
