import csv
import codecs
import sys



class CreateCSVFile:
    PASSWD = 'azerty2020@'

    @classmethod
    def read_file_csv(cls, file_csv, cohort):
        new_data = []
        try:
            with codecs.open(file_csv, encoding='utf8', errors='replace') as f:
                data = csv.reader(f, delimiter='\n')
                for r in data:
                    lname = r[0].strip().replace(' ', '')
                    fname = r[1].strip().replace(' ', '')
                    email = f"{'.'.join([fname, lname])}@archimede.online".lower()
                    username = email
                    passwd = CreateCSVFile.PASSWD
                    cohort = cohort
                    r.extend([username, email, passwd, cohort])
                    new_data.append(r)

                return new_data

        except (FileNotFoundError, TypeError) as e:
            raise Exception(e) from None

        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(file_csv, data.line_num, e))


    @classmethod        
    def create_file_csv(cls, file_csv, new_file_csv, cohort):
        try:
            data = cls.read_file_csv(file_csv, cohort)

            with codecs.open(new_file_csv, mode='w', encoding='utf8', errors='replace') as f:
                fdata = csv.writer(f, delimiter='\n', quotechar="|" )
                return fdata.writerow(','.join(data[i]) for i in range(len(data)))
        except:
            raise

        

if __name__ == "__main__":

    print(CreateCSVFile.read_file_csv('archimede.csv', '6ème'))