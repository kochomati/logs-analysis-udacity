# logs-analysis-udacity
Udacity Logs Analysis Project

### Overview
> Specific queries on a real-life database of three tables (authors, articles and log).

### Run Project

#### PreRequisites:
  - [Python3](https://www.python.org/)
  - [VirtualBox](https://www.virtualbox.org/)
  - [Vagrant](https://www.vagrantup.com/)

#### SetUp
  - Install VirtualBox and Vagrant
  - Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  - Download [sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
  - Unzip folder and place into [cloned repository](https://github.com/kochomati/logs-analysis-udacity.git)

#### Launch VM
1. Install VM from within fullstack-nanodegree-vm repository using command:
  ```
    $ vagrant up
  ```
  2. Then connect to VM using command:

  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.
  ```
    $ cd /vagrant
  ```

####Connect to database
1. Load database:
  ```
    psql -d news -f newsdata.sql
  ```
2. Connect to database:
  ```
    psql -d news
  ```
3. Run SQL statements found inside news.py in terminal or exit psql and run news.py for output:
```
  python news.py
```
