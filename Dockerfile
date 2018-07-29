FROM python:3.6.2

RUN apt-get update \
 && apt-get install -y \
      git \
      unzip \
 && rm -rf /var/lib/apt/lists/*

# install font for matplotlib
WORKDIR /usr/share/fonts
ENV RICTY_DIMINISHED_VERSION 3.2.4
ADD https://github.com/mzyy94/RictyDiminished-for-Powerline/archive/$RICTY_DIMINISHED_VERSION-powerline-early-2016.zip .
RUN unzip -jo $RICTY_DIMINISHED_VERSION-powerline-early-2016.zip \
 && fc-cache -fv

# config for matplotlib
WORKDIR /etc
RUN echo "backend : Agg" >> matplotlibrc \
 && echo "font.family : Ricty Diminished" >> matplotlibrc

WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app

# CMD [ "python", "run.py" ]