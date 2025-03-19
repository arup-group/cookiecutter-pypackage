# Updating your project

This repository isn't just for creating your project in the first place.
It can be used to update your project when fixes / features are added to the template *and* to update your project when you change your mind about the input parameters you used when you [generated your project][step-2-generate-your-package].

!!! note
    There is a limit to how well Copier can apply updates / changes to input parameters.
    More likely than not, it will produce inline merge conflicts for things it tried to implement, but failed to merge in.
    These merge conflicts are similar to when merging GitHub branches.
    VSCode (and other IDEs) offers a visual interface for resolving those conflicts.

!!! info
    You can run updates from within your project's [development environment](tutorial.md#step-6-create-a-development-environment-for-your-project) since `copier` is installed into it.

## Keeping your project up-to-date

We may make changes to this template that you want to pull into your project after you have generated it.
Copier allows you to do this, and one of your project's CI workflows will verify whether there are new template updates that you might like to merge in.

Check if there are updates:

``` bash
copier update --pretend --skip-answered
```

Apply any updates that exist:

``` bash
copier update --skip-answered
```

## Changing input arguments after project generation

You can change your mind on the [input arguments](./configuration.md) you gave when initialising the project and use `copier` to update them.

Changing some inputs will cause you less trouble than others.
For example, changing the email associated with the project will probably be seamless.
Changing whether to include a CLI or example notebooks, however, may not be.
This is because these changes entail the deletion of files / directories when you do not want them.

If you are finding it difficult to make a change, you can try generating a _new_ project with your preferred input parameters and then porting across the changes.

!!! example

    To update your project to upload the package to both an Anaconda channel and to PyPI:

    ``` bash
    copier update --data upload_conda_package="y" upload_pip_package="y"
    ```

!!! info

    For more info, see the [Coper documentation](https://copier.readthedocs.io/en/stable/updating/#never-change-the-answers-file-manually)
