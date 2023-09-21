class basic_animal(object) :
    def __init__ (self) :
        pass

def animal_class_factory(self, class_prop, keyDNA_prop):
    _d = {"DNA" : {}}
    _li = []
    _li_prohibited = ["DNA","type_animal","init","__init__","say_name","__str__","__setattr__"]
    for key in class_prop.keys() :
        _d[key] = class_prop[key]
        _li_prohibited.append (key)

    for key in keyDNA_prop :
            _d["DNA"][key] = None
            _li.append (key)
            _li_prohibited.append (key)
    

#=====================================================================================#
            
    def __init__(self, color, *DNA_prop): #color was hier origineel arg voor als je dieren maakt zonder kleur (output veranderd dus veranderd naar color (EERST: TypeError missing a required argument: 'arg'), NU: TypeError missing a required argument: 'color')
        x = 1
        self.DNA[_li[0]] = color
        setattr (self, _li[0], color)
        for item in DNA_prop :
            self.DNA[_li[x]] = item
            setattr (self, _li[x], item)
            x += 1
        #print (self.DNA)
        for key in self.DNA.keys () :
            setattr (self, key, self.DNA[key])
            
        setattr (self, "name", None)
        self.init = True

#=====================================================================================#        
            
    def __setattr__(self, item, value):
        if self.init and item in _li_prohibited :
            raise AttributeError(f"can't set attribute {item}")
        else :
            self.__dict__[item] = value

#=====================================================================================#
            
    def __add__ (self, second) :
        a=1

#=====================================================================================#
        
    def string_name (self) :
        string = f"{self.type_animal}("
        for item in self.DNA :
            string = string + item +"="+ self.DNA[_li[0]]
            break
        if len (self.DNA) > 1 :
            x = 0
            for item in self.DNA :
                if x != 0 :
                    string = string + "," + item +"="+ self.DNA[_li[x]]
                x += 1
        string = string + ")"
        return string

#=====================================================================================#
    
    def rename (self, new_name) :
        name = new_name

#=====================================================================================#
        
    def sayname (self) :
        if self.name != None : 
            print ("My name is {0}, My name is {0}, my name is {1}".format (self.sound,self.name))
        else :
            print (f"{self.sound}???")

#=====================================================================================#

    _d["type_animal"] = self
    _d["init"] = False
    _d["__init__"] = __init__
    _d["name"]     = rename
    _d["say_name"] = sayname
    _d["__str__"] = string_name
    _d["__setattr__"]= __setattr__
    print (_d)
    animal = type(self, (basic_animal, ), _d)
    return animal


#--------------------------------------------------------------------------------#
# TESTCODE
if __name__ == '__main__':
  Dog = animal_class_factory('Dog', {'sound':'WAF'}, ('color', 'eye_color'))
  print ("----------------------")
  print (Dog.__dict__)
  print(type(Dog))

  try:
    d = Dog()
  except TypeError as e:
    print(type(e).__name__, e)

  d1 = Dog('wit', 'rood')
  print (d1.__dict__)
  print(d1)
  print(type(d1))
  print(d1.color, d1.eye_color)
  print(d1.sound)

  try:
    d1.color = 'zwart'
  except AttributeError as e:
    print(type(e).__name__, e)
  try:
    d1.sound = 'woeferdewoef'
  except AttributeError as e:
    print(type(e).__name__, e)

  d1.say_name()
  d1.name = 'Theodoor'
  print(d1.name)
  d1.say_name()
  
  d1.hoedje_op = True
  print(d1.hoedje_op)
  d1.hoedje_op = False
  print(d1.hoedje_op)
  
  d2 = Dog('bruin', 'blauw')
  print(d2)
"""
  db1 = d1 + d2
  print(db1)
  db2 = d1 + d2
  print(db2)
  print(db1 is db2)
  print(type(db1) == type(db2) == type(d1) == type(d2))
  [print(d1 + d2) for _ in range(5)]
  
  Fish = animal_class_factory('Fish',
                              {'sound':'blub', 'eggshell':'soft'},
                              ('color', 'watertype', 'max_swim_speed'))
  f = Fish('goud', 'zoet', 5)
  print(f)
  print(f.sound, f.eggshell)
  try:
    f.max_swim_speed = 6
  except AttributeError as e:
    print(type(e).__name__, e)
  f.name = 'Fabritia'
  f.say_name()
  f.name = 'Fibrotio'
  f.say_name()
  df = f + db1
  print(df)
  print(df.sound)
  print(df.eggshell)
  print(type(df))

'''
output moet zijn:

<class 'type'>
TypeError missing a required argument: 'color'
Dog(color='wit', eye_color='rood')
<class '__main__.Dog'>
wit rood
WAF
AttributeError can't set attribute 'color'
AttributeError can't set attribute 'sound'
WAF ???
Theodoor
my name is WAF, my name is WAF, my name is   Theodoor
True
False
Dog(color='bruin', eye_color='blauw')
Dog(color='wit', eye_color='rood')
Dog(color='bruin', eye_color='rood')
False
True
Dog(color='wit', eye_color='blauw')
Dog(color='wit', eye_color='blauw')
Dog(color='wit', eye_color='blauw')
Dog(color='wit', eye_color='rood')
Dog(color='bruin', eye_color='blauw')
Fish(color='goud', watertype='zoet', max_swim_speed=5)
blub soft
AttributeError can't set attribute 'max_swim_speed'
my name is blub, my name is blub, my name is   Fabritia
my name is blub, my name is blub, my name is   Fibrotio
DogFish(max_swim_speed=5, color='goud', eye_color='rood', watertype='zoet')
WAFblub
soft
<class '__main__.DogFish'>
'''
"""
