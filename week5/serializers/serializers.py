import json
from pprint import pprint


class JsonableMixin:
    serializable_types = (
        int,
        float,
        str,
        list,
        bool,
        dict,
        type(None),
    )
    
    def to_json(self, indent=4):
        json_dict = {}
        name = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, JsonableMixin):
                json_dict['dict'][key] = json_dict['dict'][key].to_json()
            elif type(value) in self.serializable_types:
                json_dict[key] = value
            else:
                raise ValueError(f'{v} is not Serializable!')
        return {'class_name': name, 'dict': json_dict}

    @classmethod
    def from_json(cls, json_string, gl=globals()):
        class_dict = json.loads(json_string)[0]
        
        


class XmlableMixin:
    def to_xml(self):
        pass

    @classmethod
    def from_xml(cls, xml_string):
        pass


class Panda(JsonableMixin, XmlableMixin):
    x = globals()

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def printt(self):
        pprint.pprint(locals())


class Person(JsonableMixin, XmlableMixin):
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def __eq__(self, other):
        return self.name == other.name and self.pet == other.pet


if __name__ == '__main__':
    p = Panda(5)
    pesho = Person('pesho', p)
    print(pesho.to_json())
    p.from_json("[{\"dict\": {\"name\": 5}, \"class_name\": \"Panda\"}]")
    # pprint(globals())


def main():
    print(globals())


if __name__ == '__main__':
    main()