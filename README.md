# Python Stress Generator

### Docker
```bash
docker build -t stress_generator:latest -f Dockerfile .

docker run -d \
--env-file .env \
--name stress_generator \
stress_generator:latest
```
