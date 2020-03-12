cd ./eaw_godot_doc_module_source/egdocs/xml_docs/xml_data

del data.tar.gz

cd data

7z a -ttar data.tar ./*
7z a -tgzip ../data.tar.gz data.tar

del data.tar

pause
exit
