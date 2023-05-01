# Build the image

```
docker build -t registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-randomizers/iranthology:0.0.1 .
```

docker run -p 8888:8888 --rm -ti -w /workspace -v ${PWD}:/workspace --entrypoint jupyter registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-randomizers/iranthology:0.0.1 notebook --allow-root --ip 0.0.0.0

# Test that dataset creation works

```
tira-run \
    --output-directory ${PWD}/iranthology-dataset-tira \
    --image registry.webis.de/code-research/tira/tira-user-ir-lab-sose-2023-randomizers/iranthology:0.0.1 \
    --allow-network true \
    --command '/irds_cli.sh --ir_datasets_id iranthology-randomizers --output_dataset_path $outputDir'
```

# Test that retrieval works

```
tira-run \
    --input-directory ${PWD}/iranthology-dataset-tira \
    --image webis/tira-ir-starter-pyterrier:0.0.1-base \
    --command '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/full-rank-pipeline.ipynb'
```
