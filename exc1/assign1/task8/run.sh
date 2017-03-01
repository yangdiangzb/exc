hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
  -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
  -D stream.map.output.field.separator=' ' \
  -D stream.num.map.output.key.fields=2 \
  -D mapreduce.map.output.key.field.separator=' ' \
  -D mapreduce.partition.keycomparator.options=-k2,2nr \
  -D mapreduce.job.reduces=1 \
  -input /user/s1626297/assignment1/task7/ \
  -output /user/s1626297/assignment1/task8 \
  -mapper mapper.py \
  -file mapper.py \
  -reducer reducer.py \
  -file reducer.py