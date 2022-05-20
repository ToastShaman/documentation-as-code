FROM python:3.10.4-alpine3.15
RUN apk add --update --no-cache graphviz ttf-freefont coreutils
WORKDIR /diagrams
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
