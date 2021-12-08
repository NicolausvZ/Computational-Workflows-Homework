FROM ubuntu:21.04

RUN apt-get -y update && \
    apt-get install -y python3-minimal python3-ipython python3-pytest python3-numpy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ADD . .
RUN pip install -r requirements.txt
CMD ["python","-m","unittest","discover","-s","Tests"]
# just added a comment