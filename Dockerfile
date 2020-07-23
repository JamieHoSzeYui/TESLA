FROM elytra8/tesla:latest

RUN mkdir /TESLA && chmod 777 /TESLA
ENV PATH="/TESLA/bin:$PATH"
WORKDIR /TESLA

RUN git clone https://github.com/ElytrA8/TESLA -b TESLA /TESLA
#
#setup transfer
#
RUN curl -sL https://git.io/file-transfer | sh
#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /TESLA/

#
# Finalization
#
CMD ["python3","-m","userbot"]
