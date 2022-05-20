FROM openjdk:14-jdk-alpine3.10
ENV PLANTUML_VERSION=1.2022.5
ENV LANG en_US.UTF-8
RUN \
  apk add --no-cache graphviz wget ca-certificates && \
  apk add --no-cache graphviz wget ca-certificates terminus-font ttf-inconsolata ttf-dejavu fontconfig && \
  fc-cache -fv && \
  mkdir /app && \
  wget "https://github.com/plantuml/plantuml/releases/download/v${PLANTUML_VERSION}/plantuml-${PLANTUML_VERSION}.jar" -O /app/plantuml.jar && \
  apk del wget ca-certificates
RUN ["java", "-Djava.awt.headless=true", "-jar", "/app/plantuml.jar", "-version"]
RUN ["dot", "-version"]
ENTRYPOINT ["java", "-Djava.awt.headless=true", "-jar", "/app/plantuml.jar", "-p"]
CMD ["-tsvg"]
