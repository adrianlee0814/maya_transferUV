import maya.cmds as cmds

#list selected items
sel = cmds.ls(sl=1)

#get the shape tabs of selected items
shapes = cmds.listRelatives(sel[1], shapes=1)


for i in shapes:
	#check if said Shape is the Original 
    if 'Orig' in i:
        cmds.setAttr(i+'.intermediateObject', 0)

		#transfer attributes from first selection (sel[0]) to second selection (i)
        cmds.transferAttributes(sel[0], i, transferUVs = 2, spa = 5)
        
		#delete construction history aka Type history on Orig (does not mess with Rig)
        cmds.delete(i, ch = 1)
        cmds.setAttr(i+'.intermediateObject', 1)
        print 'Transferred attribute from ' + sel[0] + ' and deleted construction history of ' + i
        
