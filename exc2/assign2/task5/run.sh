hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.reduces=1 \
-input /data/assignments/ex2/part3/webLarge.txt \
-output /user/s1626297/assignment2/task5 \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py