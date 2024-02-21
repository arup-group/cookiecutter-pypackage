# Updating your project

This repository isn't just for creating your project in the first place.
It can be used to update your project when fixes / features are added to the template *and* to update your project when you change your mind about the input parameters you used when you [generated your project][step-2-generate-your-package].

!!! note
    There is a limit to how well Cruft can apply updates / changes to input parameters.
    More likely than not, it will produce a lot of `.rej` files explaining what updates it tried to implement, but failed to merge in.
    You will need to go through each of these manually and make the changes in the corresponding source code file.

    After each change, delete the corresponding `.rej` file.
    Your project will not let you commit changes if `.rej` files are still present.

!!! info
    You can run updates from within your project's [development environment](tutorial.md#step-6-create-a-development-environment-for-your-project) since `cruft` is installed into it.

## Keeping your project up-to-date

We may make changes to this template that you want to pull into your project after you have generated it.
Cruft allows you to do this, and one of your project's CI workflows will verify whether there are new template updates that you might like to merge in.

Check if there are updates:

``` bash
cruft check
```

View the diff between your project and the most up-to-date template:

``` bash
cruft diff
```

Apply any updates that exist:

``` bash
cruft update
```

## Changing input parameters after project generation

You can change your mind on the [input parameters][configuration-values] you gave when initialising the project and use `cruft` to update them.

Changing some inputs will cause you less trouble than others.
For example, changing the email associated with the project will probably be seamless.
Changing whether to include a CLI or example notebooks, however, may not be.
This is because these changes entail the deletion of files / directories when you do not want them.

If you are finding it difficult to make a change, you can try generating a _new_ project with your preferred input parameters and then porting across the changes (make sure to update the parameter values in your initial project's `cruft.json` file.).

!!! example

    To update your project to upload the package to both an Anaconda channel and to PyPI:

    ``` bash
    cruft update --variables-to-update '{ "upload_conda_package" : "y" , "upload_pypi_package": "y"}'
    ```

!!! info

    For more info, see the [Cruft documentation](https://cruft.github.io/cruft/#updating-values-of-template-variables)