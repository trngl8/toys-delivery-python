## Contributors instructions for the Triangle Software members


### How to install and work

```bash
$ git clone git@github.com:trngl8/toys-delivery-python.git
$ cd toys-delivery-python
$ git checkout develop
$ git checkout -b your_branch_name
```

### How to make a new feature

You in a working directory 

```bash
$ git checkout develop
$ git pull 
$ git checkout your_branch_name
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