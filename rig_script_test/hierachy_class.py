import maya.cmds as cmds

class MakeHierachy():
    def execute_creating_joint(self):
        self.create_root_joint()
        self.create_main_joint()
        self.create_upper_body_joint()
        self.create_arms_joint(pos="R")
        self.create_arms_joint(pos="L")
        self.create_finger_joint(pos="R")
        self.create_finger_joint(pos="L")
        self.create_legs_joint(pos="R")
        self.create_legs_joint(pos="L")
        
    def create_child_joint(self, parent, childeren):
        """
        This function takes parent and childeren as params 
        """
        if not cmds.objExists(f"{parent}_joint"):
            parent_joint = cmds.joint(name=f"{parent}_joint")
            print("parent",parent_joint)
            for child in childeren:
                child_joint = cmds.joint(name=f"{child}_joint")
                print("child",child_joint)
                cmds.parent(child_joint, world=True)
                cmds.parent(child_joint, parent_joint)
        else:
            for child in childeren:
                child_joint = cmds.joint(name=f"{child}_joint")
                print("child",child_joint)
                cmds.parent(child_joint, world=True)
                cmds.parent(child_joint, f"{parent}_joint" )

    def create_root_joint(self):
        self.create_child_joint(parent="root",childeren=["main"])
    
    def create_main_joint(self):
        self.create_child_joint(parent="main", childeren=["spine1","pelvis"])
    
    def create_upper_body_joint(self):
        upper_body_hierachy = {"spine1":"spine2","spine2":"spine3","spine3":"neck","neck": "head"}
        for p , c in upper_body_hierachy.items():
            self.create_child_joint(parent=f"{p}",childeren=[f"{c}"])

    def create_arms_joint(self,pos):
        arms_hierachy = {"spine3":f"{pos}_clavicle",
                         f"{pos}_clavicle":f"{pos}_shoulder",
                         f"{pos}_shoulder":f"{pos}_elbow",
                         f"{pos}_elbow":f"{pos}_hand"}
        for p , c in arms_hierachy.items():
            self.create_child_joint(parent=f"{p}",childeren=[f"{c}"])

    def create_finger_joint(self,pos):
        thumb_hierachy = {f"{pos}_hand":f"{pos}_thumb1",f"{pos}_thumb1":f"{pos}_thumb2",f"{pos}_thumb2":f"{pos}_thumb3"}
        index_hierachy = {f"{pos}_hand":f"{pos}_index1",f"{pos}_index1":f"{pos}_index2",f"{pos}_index2":f"{pos}_index3"}
        picky_hierachy = {f"{pos}_hand":f"{pos}_picky1",f"{pos}_picky1":f"{pos}_picky2",f"{pos}_picky2":f"{pos}_picky3"}
        hierachy_list = [thumb_hierachy,index_hierachy,picky_hierachy]
        for hierachy in hierachy_list:
            for p , c in hierachy.items():
                self.create_child_joint(parent=f"{p}",childeren=[f"{c}"]) 

    def create_legs_joint(self,pos):

        legs_hierachy = {"pelvis":f"{pos}_but",
                         f"{pos}_but":f"{pos}_knee",
                         f"{pos}_knee":f"{pos}_foot",
                         f"{pos}_foot":f"{pos}_toe"}
        for p , c in legs_hierachy.items():
            self.create_child_joint(parent=f"{p}",childeren=[f"{c}"])

r = MakeHierachy()
r.execute_creating_joint()

