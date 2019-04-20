Instruction for scraping script

To start scraping, use system command line

python scrape_main.py <your api key> <request page start> <request page finish> <articles subject> <request dumpfile name> <csv dataset name>

You will get most cited articles for each year among 2010-2019 on requested pages using article subject you have chosen.

The list of associated article subject tags can be found on subjects.txt file.

After that, all metadata will be retrieved. You may want to retrive autorships and citations data for corresponding graphs. This can be done by adding these arguments to your command line request

- --autorships True --autorships_dump <dumpfile>
- --citations True --citations_dump <dumpfile> --citations_start <citation start index> --citations_start <citation finish index>
