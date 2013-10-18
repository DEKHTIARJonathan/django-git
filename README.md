README
======

## Install

### From the Original Creator, Seth

Get the latest source code from Seth's `git` repo with:

    git checkout git://github.com/sethtrain/django-git.git

### From an Bleeding Edge Fork, by Hobson

Add a line in requirements.txt pointing to Hobson's github fork:

    -e git+git://github.com/hobsonlane/django-git.git@master#egg=django-git-0.1.1>=0.1.1

Then install your requirements.txt to your virtualenv as usual, using `pip`:

    pip install -r requirements.txt

### Configure

Add the django-git/django_git folder to your PYTHONPATH.

Add `"django_git"` to your INSTALLED_APPS in your Django project settings.py. Also add a line to settings.py to point django-git to the repositories you want to serve up:

    REPOS_ROOT = '/Users/seth/projects/git'

Include the django-git urls.py:

    urlpatterns = patterns('',
        ...
        (r'^git/', include('django_git.urls')),
        ...
    )

Make sure AppDirectoriesFinder is in `STATICFILES_FINDERS` in your `settings.py`, then collect the static files (unless staticfiles is a part of your production stack): 

    ./manage.py collectstatic -n
    # And if that outputs some js/jquery-1.2.6.min.js file and our js/commit.js, continue
    ./manage.py collectstatic

If there are name resolution issues with commit.js, rename it in templates/django_git/commit.html and move it appropriately.

With the use of [auto_render](http://djangosnippets.org/snippets/559/), using this app in other projects/apps is much simpler. Apps, not wanting to show the repo/commit/blob directly but handle them in their own way, can simply call the view with only_context=True:

    @auto_render
    def some_other_view(request, repo='', commit_id='')
        if not commit_id or not repo: raise Http404

        ctx = django_git.views.commit(request, repo, commit_id, only_context=True)
        diffs = ctx['diffs']
        ...
        # Though a more direct use of django_git.utils could be used if necessary as well:
        diffs = django_git.utils.get_commit(repo,commit).diffs


Requirements

* Pygments
* GitPython
* Django 1.3 (alpha or better)

If you would like to get started with django-git [Hugh Brown](http://github.com/hughdbrown) has created [Django-git-tester](http://github.com/hughdbrown/Django-git-tester).

Thanks!
-------
* Christos Trochalakis
* Hugh Brown
* Fahrzin Hemmati
