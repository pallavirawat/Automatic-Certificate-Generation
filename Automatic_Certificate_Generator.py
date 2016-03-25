#!/usr/bin/env python
from gimpfu import *
import os
def run(*args):
    template_file,list_file,output_folder=args
    output_folder=os.path.expanduser('~/'+output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    i=0
    with open(list_file,'r') as list:
        for name in list:
            i+=1;
            bg_image=pdb.gimp_file_load(template_file,template_file)
            name_layer=filter(lambda x: x.name == '<name>',bg_image.layers)[0]
            pdb.gimp_text_layer_set_font(name_layer,'Comic Sans MS')
    
            pdb.gimp_text_layer_set_font_size(name_layer,116,0) #Change how name (from input will appear. Eg. Size,Font etc
            pdb.gimp_text_layer_set_text(name_layer,name)
            merged = pdb.gimp_image_merge_visible_layers(bg_image,0)
            output_filename=name+str(i)+".png"
            output_filename=os.path.join(output_folder,output_filename)
    
            pdb.file_png_save_defaults(bg_image,merged,output_filename,output_filename)
		#print "Finished"
    
register("certificate_generator","","","","","","<Toolbox>/Xtns/Languages/Python-Fu/_Certificate-Generator","",[(PF_FILE,"arg0","Certificate Template File",""),(PF_FILE,"arg1","Input Data File",""),(PF_STRING,"arg2","Output Folder","")],[],run)

main()
    
