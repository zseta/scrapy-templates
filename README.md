# scrapy-templates
Scrapy spider templates for different kinds of websites.

## How to figure out which template you need?

The quickest way is to figure out your **crawling logic** first, what requests you 
need to make to get to the data, in terms of behaviour & deepness:

### Behaviour

Behaviour describes what the spider does on the level it's on at the moment. 
This can be:

- **Extraction** (extract data fields)
- **Following** (making a request to go deeper in the website eg. from `example.com` 
  to `example.com/page`)
- **Pagination** (making a request to paginate - spider stays on the same level eg.
  from `example.com/page/1` to `example.com/page/2`)

### Deepness

Deepness means how deep your spider is at the moment (while crawling), 
relative to the start url.

For example, if your spider starts at `example.com` that's *level 0*, then you make a request on 
that page to `example.com/page`, your spider is on *level 1* now. Then, if you 
go to `example.com/page/sub-page`, that's *level 2*.

## Currently available templates

### -  [Ext.py](templates/Ext.py)
1. Extract data fields (level 0)

### - [ExtPag.py](templates/ExtPag.py)
1. Extract data fields + paginate (level 0)

### - [Fol_Ext.py](templates/Fol_Ext.py)
1. Follow urls (level 0)
2. Extract data fields (level 1)

### - [Fol_ExtPag.py](templates/Fol_ExtPag.py)
1. Follow urls (level 0)
2. Extract data fields + paginate (level 1)

### - [Fol_Fol_Ext.py](templates/Fol_Fol_Ext.py)
1. Follow urls (level 0)
2. Follow urls (level 1)
3. Extract data fields + paginate (level 2)

### - [Fol_FolPag_Ext.py](templates/Fol_FolPag_Ext.py)
1. Follow urls (level 0)
2. Follow urls + paginate (level 1)
3. Extract data fields (level 2)

### - [FolPag_Ext.py](templates/FolPag_Ext.py)
1. Follow urls + paginate (level 0)
2. Extract data fields (level 1)

### - [sitemap.py](templates/sitemap.py)
1. Extract data from sitemap

## File naming convention

Each template file name is supposed to clearly show the crawling logic of the 
spider. So once you know the crawling logic you need for the website 
and understand the naming convention of the files, you should be able to 
pick your template.

A template file's name contains all the behaviours a spider does, which can be:

- **Extraction** --> represented as `Ext` in the file name
- **Following** --> represented as `Fol` in the file name
- **Pagination** --> represented as `Pag` in the file name

Two behaviours in the file name are separated by an `_` (underscore) if the 
second behaviour is done one level deeper. If they are not separated by an 
underscore, that means they happen on the same level.

## How to contribute?

### Submit a new template
The most useful thing you can do is to submit a new sipder template which 
hasn't been made yet. You can do this by:

1. Fork this repo
2. Add the new template file you created
3. Submit a pull request according to guidelines

### Request a new template to be made
If you have an idea for a template, and you don't feel like submitting a pull 
request, create an issue about it. So maybe someone will take it and implment it.
