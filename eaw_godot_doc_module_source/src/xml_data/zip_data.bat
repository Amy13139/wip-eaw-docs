del data.tar.gz

cd data

7z a -ttar data.tar ./*
7z a -tgzip ../data.tar.gz data.tar

del data.tar
