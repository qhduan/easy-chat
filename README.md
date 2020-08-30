
```

$ wget https://gist.githubusercontent.com/qhduan/a2fb254c10ff1130d33ac2581ac9ce13/raw/0bf67fb1d9f42855e09fef0e1ce249258b52dd3e/gdown.pl
$ perl gdown.pl "https://drive.google.com/open?id=1-R2T-vVBu5aF5nKum5S9vNjDjtFJnrd4" "gpt_small_export.zip"
$ mkdir -p chat/1 && cd chat/1 && unzip ../../gpt_small_export.zip && cd ../..
$ docker build -t qhduan/gpt-chat .

# For testing
$ docker run -it --rm -p 8501:8501 qhduan/gpt-chat
$ python3 chat.py

```


