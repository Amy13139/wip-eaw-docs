del data.tar.gz

7z a -r -ttar data.tar data/*
7z a -tgzip data.tar.gz data.tar

del data.tar
