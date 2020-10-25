# COCO Exporter

## RUN

Inside this folder is a script for converting Labelbox JSON to COCO file exports. To get a JSON export file from your project,
visit the export tab of your project and select the JSON option from the dropdown. This will be the file input for the COCO converter script in this directory.

This was taken from [Labelbox repository](https://github.com/Labelbox/Labelbox.git) (all rights belongs to them).
If you wish to clone their repo then type in cmd:

```sh
git clone https://github.com/Labelbox/Labelbox.git
```

To get started you'll want to download and install Docker on your desktop.
Follow the installation and setup instructions at [docker-hub](https://www.docker.com/products/docker-desktop).

**PS:** Make sure you correctly installed Docker by running `docker` in the command line or terminal.

Once you have installed Docker, you may run the converter inside a docker container.

## For MAC and Linux Users

Right after this if you want to run the converter just type:

```sh
# e.g. if your json export file is named "export.json" and is in your Downloads directory

make run-local-export EXPORT_PATH=~/input_json/export.json OUTPUT_DEST=~/output_coco
```

**PS:** Use absolute paths in `EXPORT_PATH` and `OUTPUT_DEST` and remember to put the json file you want to transform in the `input_json` folder.

Note: The COCO export output location, if unmodified, will be saved in same directory as the input file.

```sh
# e.g. if your json export file is named "export.json" and is in your Downloads directory

make run-local-export EXPORT_PATH=~/Downloads/export.json
```

## For Windows Users

Right after cloning the git hub repo do this if you want to run the converter just type:

```sh
# e.g. if your json export file is named "export.json" and is in your Downloads directory and you wish to save in the same directory as Downloads

docker run -it --rm -v "C:\Users\xxx\Downloads:/output" -v "C:\Users\xxx\Downloads\export.json:/input" coco
```

## Notes about the exporters

The `coco_exporter.py` is the slightly modified file that helps convert the polygon annotated data json exported file from labelbox to COCO format.

# Update the JSON, load and split the data

## Order the categories 

Run the `Update_Categories_ids.ipynb` to delete the supercategory called classifications from the COCO JSON and update the order of the other supercategories.

## Load the dataset locally

To load the data locally from labelbox use the `Loading_Updating_dataset.ipynb`.

## Split the data into train and test sets

To split the data into train and test sets as well as the JSON file accordingly, use the `Update_Json_Split_Data.ipynb` notebook.




