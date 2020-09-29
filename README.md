Original Fawkes Project
------

Fawkes is a privacy protection system developed by researchers at [SANDLab](https://sandlab.cs.uchicago.edu/), University of Chicago. For more information about the project, please refer to our project [webpage](https://sandlab.cs.uchicago.edu/fawkes/). Contact us at fawkes-team@googlegroups.com. 

We published an academic paper to summarize our work "[Fawkes: Protecting Personal Privacy against Unauthorized Deep Learning Models](https://www.shawnshan.com/files/publication/fawkes.pdf)" at *USENIX Security 2020*. 

NEW! If you would like to use Fawkes to protect your identity, please check out our software and binary implementation on the [website](https://sandlab.cs.uchicago.edu/fawkes/#code). 

Copyright
---------
This code is intended only for personal privacy protection or academic research. 

Usage
-----

`$ fawkes`

Options:

* `-m`, `--mode`       : the tradeoff between privacy and perturbation size. Select from `min`, `low`, `mid`, `high`. The higher the mode is, the more perturbation will add to the image and provide stronger protection. 
* `-d`, `--directory`  : the directory with images to run protection.
* `-g`, `--gpu`        : the GPU id when using GPU for optimization.
* `--batch-size`       : number of images to run optimization together. Change to >1 only if you have extremely powerful compute power. 
* `--format`      : format of the output image (png or jpg). 

when --mode is `custom`: 
* `--th`       : perturbation threshold
* `--max-step`       : number of optimization steps to run 
* `--lr`       : learning rate for the optimization
* `--feature-extractor` : name of the feature extractor to use
* `--separate_target`   : whether select separate targets for each faces in the diectory. 

### Example

`fawkes -d ./imgs --mode min`

### Tips
- The perturbation generation takes ~60 seconds per image on a CPU machine, and it would be much faster on a GPU machine. Use `batch-size=1` on CPU and `batch-size>1` on GPUs. 
- Turn on separate target if the images in the directory belong to different people, otherwise, turn it off. 
- Run on GPU. The current Fawkes package and binary does not support GPU. To use GPU, you need to clone this, install the required packages in `setup.py`, and replace tensorflow with tensorflow-gpu. Then you can run Fawkes by `python3 fawkes/protection.py [args]`. 


### Capstone 2020

The aim of our project is to improve upon the original fawkes project by hopefully optimizing the protection process, provide a more user-friendly interface and a more accessible chrome extension distribution of the original software which hopefully can also support GPU.

Currently, we are still running test on the original Fawkes binary, namely benchmarking its runtime.

You can run it as:

> python3 Capstone2020/fawkes/protection.py -d ./imgs --mode min > {benchmark result file path}
