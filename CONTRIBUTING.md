## Contributors instructions for the Triangle Software members


### How to make a new feature

You in a working directory 

```bash
$ git checkout develop
$ git pull 
$ git checkout -b your_branch_name
```

... do you task

When you are finished:

```bash
$ git status
$ git add .
$ git commit -m "some_message_for_the_commit"
$ git push -u origin your_branch_name
```

... and create a pull request.