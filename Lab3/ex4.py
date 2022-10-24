
def build_xml_element(tag, content, **parameters):
    return "<" + tag + " " + r" ".join([p[0]+" = \"" + p[1] + "\"" if type(p[1]) == str else p[0]+" = " + str(p[1])
                                        for p in parameters.items()])+">"+content+"</"+tag+">"    
   
def main():
    print(build_xml_element("a", "Buna ziua",
          href=" http://python.org ", _class=" my-link ", id=" someid "))
    
main()
