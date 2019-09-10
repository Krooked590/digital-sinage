if [ -z $1 ] || [ -z $2 ]; then 
    exit 1
fi

python video_converter.py $1
python screenly_uploader.py $1 $2

exit 0