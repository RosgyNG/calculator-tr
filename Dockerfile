FROM alpine

RUN apk add --update --no-cache python3 git py3-colorama

RUN mkdir /tmp/calculator
RUN git clone https://github.com/RosgyNG/calculator-tr.git /tmp/calculator

RUN cp /tmp/calculator/calculator.py /usr/bin/calculator && chmod +x /usr/bin/calculator

RUN rm -rf /tmp/calculator

ENTRYPOINT [ "calculator" ]