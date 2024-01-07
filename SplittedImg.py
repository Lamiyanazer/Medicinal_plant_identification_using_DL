import splitfolders

#Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.

splitfolders.ratio(r"C:\Users\lamiy\OneDrive\Desktop\Proj_MedPlants\Medicinal Leaf Dataset\Segmented Medicinal Leaf Images", output=r"C:\Users\lamiy\OneDrive\Desktop\Proj_MedPlants\Medicinal Leaf Dataset\Splittedimages",
    seed=1337, ratio=(.8, .2), group_prefix=None, move=False) # default values