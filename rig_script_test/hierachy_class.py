
import sys
sys.path.append('D:\maya_rig_test')
import maya.cmds as cmds
from get_joint_position import JointPosCatcher

class MakeHierachy(JointPosCatcher):

    def execute_creating_joint(self):
        print("Starting joint creation process...")
        self.create_root_joint()
        self.create_main_joint()
        self.create_upper_body_joint()
        # self.create_arms_joint(pos="R")
        self.create_arms_joint(pos="L")
        # self.create_finger_joint(pos="R")
        self.create_finger_joint(pos="L")
        # self.create_legs_joint(pos="R")
        self.create_legs_joint(pos="L")
        print("Joint creation process completed.")

    def create_child_joint(self, parent, childeren):
        """
        Creates a child joint for the specified parent.
        """
        print(f"Creating child joint for parent: {parent}, children: {childeren}")
        parent_p = self.execute_get_joint_pos_function(parent)
        print(f"Parent position: {parent_p}")
        if not cmds.objExists(f"{parent}_joint"):
            parent_joint = cmds.joint(name=f"{parent}_joint", position=parent_p, radius=0.5)
            print(f"Created parent joint: {parent_joint}")
            for child in childeren:
                child_p = self.execute_get_joint_pos_function(child)
                print(f"Child {child} position: {child_p}")
                child_joint = cmds.joint(name=f"{child}_joint", position=child_p, radius=0.5)
                print(f"Created child joint: {child_joint}")
                cmds.parent(child_joint, world=True)
                cmds.parent(child_joint, parent_joint)
        else:
            print(f"{parent}_joint already exists.")
            for child in childeren:
                child_p = self.execute_get_joint_pos_function(child)
                print(f"Child {child} position: {child_p}")
                child_joint = cmds.joint(name=f"{child}_joint", position=child_p, radius=0.5)
                print(f"Created child joint: {child_joint}")
                cmds.parent(child_joint, world=True)
                cmds.parent(child_joint, f"{parent}_joint")

    def create_root_joint(self):
        print("Creating root joint...")
        self.create_child_joint(parent="root", childeren=["main"])
    
    def create_main_joint(self):
        print("Creating main joint...")
        self.create_child_joint(parent="main", childeren=["spine1", "pelvis"])
    
    def create_upper_body_joint(self):
        print("Creating upper body joints...")
        upper_body_hierachy = {
            "spine1": "spine2",
            "spine2": "spine3",
            "spine3": "neck",
            "neck": "head"
        }
        for p, c in upper_body_hierachy.items():
            print(f"Creating upper body joint for parent: {p}, child: {c}")
            self.create_child_joint(parent=p, childeren=[c])

    def create_arms_joint(self, pos):
        print(f"Creating arm joints for {pos} side...")
        arms_hierachy = {
            "spine3": f"{pos}_clavicle",
            f"{pos}_clavicle": f"{pos}_shoulder",
            f"{pos}_shoulder": f"{pos}_elbow",
            f"{pos}_elbow": f"{pos}_wrist",
            f"{pos}_wrist": f"{pos}_hand"
        }
        for p, c in arms_hierachy.items():
            print(f"Creating arm joint for parent: {p}, child: {c}")
            self.create_child_joint(parent=p, childeren=[c])

    def create_finger_joint(self, pos):
        print(f"Creating finger joints for {pos} side...")
        thumb_hierachy = {
            f"{pos}_hand": f"{pos}_thumb1",
            f"{pos}_thumb1": f"{pos}_thumb2",
            f"{pos}_thumb2": f"{pos}_thumb3"
        }
        index_hierachy = {
            f"{pos}_hand": f"{pos}_index1",
            f"{pos}_index1": f"{pos}_index2",
            f"{pos}_index2": f"{pos}_index3"
        }
        picky_hierachy = {
            f"{pos}_hand": f"{pos}_pinky1",
            f"{pos}_pinky1": f"{pos}_pinky2",
            f"{pos}_pinky2": f"{pos}_pinky3"
        }

        hierachy_list = [thumb_hierachy, index_hierachy, picky_hierachy]
        for hierachy in hierachy_list:
            for p, c in hierachy.items():
                print(f"Creating finger joint for parent: {p}, child: {c}")
                self.create_child_joint(parent=p, childeren=[c])

    def create_legs_joint(self, pos):
        print(f"Creating leg joints for {pos} side...")
        legs_hierachy = {
            "pelvis": f"{pos}_but",
            f"{pos}_but": f"{pos}_knee",
            f"{pos}_knee": f"{pos}_foot",
            f"{pos}_foot": f"{pos}_ankle",
            f"{pos}_ankle": f"{pos}_toe"
        }
        for p, c in legs_hierachy.items():
            print(f"Creating leg joint for parent: {p}, child: {c}")
            self.create_child_joint(parent=p, childeren=[c])

joint_maker = MakeHierachy()
joint_maker.execute_creating_joint()
