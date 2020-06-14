# BC's Git Style Guide

### Cruddy Commit Messages
1\) Begin each commit message with one of three [CRUD](https://idratherbewriting.com/learnapidoc/api-glossary.html#crud)-oriented _commit directives_:  

* CREATE
* UPDATE
* DELETE

2\) Use CREATE, UPDATE, and DELETE for both files and file content.

3\) For files, CREATE, UPDATE, and DELETE mean the following:
  * CREATE—add one or more new files
  * UPDATE—rename one or more existing files
  * DELETE—delete one or more existing files

4\) For file content, CREATE, UPDATE, and DELETE mean the following:

  * CREATE—add new content to a file
  * UPDATE—modify existing file content
  * DELETE—delete file content

5\) Follow each commit directive with a list of _commit items_ to which the directive applies.

  * If a commit directive applies to one or more files, use the word _files_ as a single commit item. Examples:

    * CREATE files
    * UPDATE files
    * DELETE files


  * If a commit directive applies to file content, list brief descriptions of the content elements that the commit will change (comma separated, no conjunctions). Examples:

    * CREATE subheading for second section, unordered list in first section
    * UPDATE second paragraph in second section
    * DELETE third section

6\) Small additions to file content may be listed as UPDATE commit items only if the additions relate directly to  modifications.

7\) If a commit directive applies to both files and file content, list the word _files_ first. Examples:

  * CREATE files, footnotes section
  * DELETE files, archived comments

8\) Explanations and clarifications for commit items are optional.

9\) When included, an explanation or  clarification should (1) appear in parentheses, (2) relate only to the immediately preceding commit item, and (3) consist of only a descriptive word or phrase. Examples:

  * CREATE files (for appointments), appointment entries
  * UPDATE second paragraph in second section (add links)
  * DELETE third paragraph (redundant)

10\) Include file descriptions (or file names—see below) only in parentheses. Examples:

  * UPDATE carousel (on documents page)
  * DELETE third paragraph (on home page)

11\) List multiple commit directives within a single commit message in the following order:

  1. CREATE
  2. UPDATE
  3. DELETE

12\) Separate multiple directives within a single commit message with semicolons. Example:

  * CREATE files (for new website section); UPDATE second paragraph (in history section); DELETE files (temporary), email addresses (on contact page)

13\) Use double quotes to enclose commit messages on the command line.

14\) Use single quotes within commit messages to indicate exact names. Example:

  * CREATE files ('MyClass.java')
  * UPDATE files (renamed 'myOldFileName.js' to 'myNewFileName.js')
  * DELETE files ('my_module.py')

15\) Do not end commit messages with a period or any other punctuation mark.

16\) Limit commit messages to fewer than 50 words.
