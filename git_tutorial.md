# CourseInvestments
Repository of the exercise done for the investments course from the master of financial engineering EPFL.

## Basic tutorial for git
All the command below have to be done (written in) from your command line, terminal. And when typing it in your terminal, your terminal should be in you git folder.


# Initialise the git on your computer
git clone https://github.com/tombenamato/CourseInvestments.git

# Starting to work
git pull
/// it will download the last version
# uploading your work online
git pull

git commit -am" the message"

/// It will commit, save your work in the git forverer, i.e. we can go back to this if we want

/// -a mean all the file of the folder is save/commited, -m"" is to write a message so we know if we want to go back to a saved state which one it is. Also it enable others, to follow what you have done more easily

git push

/// upload your local git online, so everyone have your last git (with all it's history)

# in case of conflict
First call Thomas Bienaimé, as it might be easy.

If you know you didn't do any work and just want to start from what is online do the following

git reset --hard

/// it will reset to the online version, so every work you have not uploaded event if commited locally WILL DISAPEAR

git pull

//// normally now you have the online code
