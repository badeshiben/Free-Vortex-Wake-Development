from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from io import open
from builtins import map
from builtins import range
from builtins import chr
from builtins import str
from future import standard_library
standard_library.install_aliases()

from .File import File, WrongFormatError, BrokenReaderError
from .CSVFile import CSVFile
import numpy as np
import pandas as pd
import struct
import os
import re

from .wetb.fast import fast_io



# --------------------------------------------------------------------------------}
# --- OUT FILE 
# --------------------------------------------------------------------------------{
class FASTOutFile(File):

    @staticmethod
    def defaultExtensions():
        return ['.out','.outb','.elm','.elev']

    @staticmethod
    def formatName():
        return 'FAST output file'

    def _read(self):
        def readline(iLine):
            with open(self.filename) as f:
                for i, line in enumerate(f):
                    if i==iLine-1:
                        return line.strip()
                    elif i>=iLine:
                        break



        ext = os.path.splitext(self.filename.lower())[1]
        self.info={}
        try:
            if ext in ['.out','.elev']:
                self.data, self.info = fast_io.load_ascii_output(self.filename)
            elif ext=='.outb':
                self.data, self.info = fast_io.load_binary_output(self.filename)
            elif ext=='.elm':
                F=CSVFile(filename=self.filename, sep=' ', commentLines=[0,2],colNamesLine=1)
                self.data = F.data
                del F
                self.info['attribute_units']=readline(3).replace('sec','s').split()
                self.info['attribute_names']=self.data.columns.values
            else:
                self.data, self.info = fast_io.load_output(self.filename)
        except MemoryError as e:    
            raise BrokenReaderError('FAST Out File {}: Memory error encountered\n{}'.format(self.filename,e))
        except Exception as e:    
            raise WrongFormatError('FAST Out File {}: {}'.format(self.filename,e.args))

        if self.info['attribute_units'] is not None:
            self.info['attribute_units'] = [re.sub('[()\[\]]','',u) for u in self.info['attribute_units']]


    #def _write(self): # TODO
    #    pass

    def _toDataFrame(self):
        if self.info['attribute_units'] is not None:
            cols=[n+'_['+u.replace('sec','s')+']' for n,u in zip(self.info['attribute_names'],self.info['attribute_units'])]
        else:
            cols=self.info['attribute_names']
        if isinstance(self.data, pd.DataFrame):
            df= self.data
            df.columns=cols
        else:
            df = pd.DataFrame(data=self.data,columns=cols)

        return df


if __name__ == "__main__":
    B=FASTOutFile('Turbine.outb')
    print(B.data)



