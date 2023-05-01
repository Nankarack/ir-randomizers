FROM webis/tira-ir-datasets-starter:0.0.47

# add jupyter so that we can run a notebook directly in the container
RUN apk add libffi-dev && pip3 install jupyter

COPY notebook.ipynb ir-anthology-processed.jsonl topics.xml iranthology.py /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/

ENTRYPOINT [ "/irds_cli.sh" ]

