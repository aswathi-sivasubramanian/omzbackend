FROM  python:3.8.13-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /omzbackend
# copy from the current directory of the Dockerfile to /mamba-backend in the image
COPY . .
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh

RUN ls -a
RUN sed -i -e 's/\r$//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown nobody /entrypoint.sh

EXPOSE 8080