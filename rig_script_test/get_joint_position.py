import maya.cmds as cmds
from position_collector import PositionCollector
from mesh_finder import MeshFinder

class JointPosCatcher(PositionCollector, MeshFinder):
    """
    The JointPosCatcher class calculates joint positions by referencing mesh objects.
    It inherits from PositionCollector and MeshFinder to extend its functionality 
    and calculate different joint positions within the rigging pipeline.
    """
    def execute_get_joint_pos_function(self, name):
        """
        """
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        try:
            
            joint_function = getattr(self, f"get_{name}_joint_pos")
            p = joint_function()
            return p
        except AttributeError:
            print(f"Error: '{name}'there's no function!!!")
            return None
    
    ####################################################################
    # root
    def get_root_joint_pos(self):
        """
        Returns the root joint position.
        
        :rtype: tuple
        :return: Tuple representing the root joint position at (0, 0, 0)
        """
        p = (0, 0, 0)
        print(p)
        return p

    ####################################################################
    # main
    def get_main_joint_pos(self):
        """
        Retrieves the position of the 'pelvis' mesh and calculates its half position.

        :rtype: tuple
        :return: Tuple representing the half position of the 'pelvis' mesh
        """
        print("Retrieving main joint (pelvis) position...")
        mesh = self.find_meshes_with_name("*pelvis*")
        print(f"Pelvis mesh found: {mesh}")
        p = self.get_half_positions(mesh)
        print(f"Main joint position: {p}")
        return p


    ####################################################################
    # body
    def get_spine1_joint_pos(self):
        """
        Retrieves the position of the 'spine1' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'spine1' mesh
        """
        mesh = self.find_meshes_with_name("*spine1*")
        p = self.get_half_positions(mesh)
        return p

    def get_spine2_joint_pos(self):
        """
        Retrieves the position of the 'spine2' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'spine2' mesh
        """
        mesh = self.find_meshes_with_name("*spine2*")
        p = self.get_half_positions(mesh)
        return p

    def get_spine3_joint_pos(self):
        """
        Retrieves the position of the 'spine3' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'spine3' mesh
        """
        mesh = self.find_meshes_with_name("*_spine3*")
        p = self.get_half_positions(mesh)
        return p

    def get_neck_joint_pos(self):
        """
        Retrieves the position of the 'neck' mesh and calculates its bottom center position.
        
        :rtype: tuple
        :return: Tuple representing the bottom center position of the 'neck' mesh
        """
        mesh = self.find_meshes_with_name("*_neck*")
        p = self.get_pos_bottom_center(mesh)
        return p

    def get_head_joint_pos(self):
        """
        Retrieves the position of the 'head' mesh and calculates its bottom center position.
        
        :rtype: tuple
        :return: Tuple representing the bottom center position of the 'head' mesh
        """
        mesh = self.find_meshes_with_name("*_head*")
        p = self.get_pos_bottom_center(mesh)
        return p

    def get_pelvis_joint_pos(self):
        """
        Retrieves the position of the 'head' mesh and calculates its bottom center position.
        
        :rtype: tuple
        :return: Tuple representing the bottom center position of the 'head' mesh
        """
        mesh = self.find_meshes_with_name("*_pelvis*")
        p = self.get_pos_bottom_center(mesh)
        return p

    ####################################################################
    # arms
    def get_L_clavicle_joint_pos(self):
        """
        Retrieves the position of the 'spine3' mesh and calculates its quarter top position.
        
        :rtype: tuple
        :return: Tuple representing the quarter top position of the 'spine3' mesh
        """
        mesh = self.find_meshes_with_name("*_spine3*")
        p = self.get_pos_quater_top_(mesh)
        return p

    def get_L_shoulder_joint_pos(self):
        """
        Retrieves the position of the 'L_shoulder' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_shoulder' mesh
        """
        mesh = self.find_meshes_with_name("*_L_shoulder*")
        p = self.get_half_positions(mesh)
        return p

    def get_L_elbow_joint_pos(self):
        """
        Retrieves the position of the 'L_elbow' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_elbow' mesh
        """
        mesh = self.find_meshes_with_name("*_L_elbow*")
        p = self.get_half_positions(mesh)
        return p

    def get_L_wrist_joint_pos(self):
        """
        Retrieves the position of the 'L_wrist' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_wrist' mesh
        """
        mesh = self.find_meshes_with_name("*_L_wrist*")
        p = self.get_half_positions(mesh)
        return p

    def get_L_hand_joint_pos(self):
        """
        Retrieves the position of the 'L_hand' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_hand' mesh
        """
        mesh = self.find_meshes_with_name("*_L_hand*")
        p = self.get_half_positions(mesh)
        return p

    ####################################################################
    # fingers
    def get_L_thumb_joints_pos(self):
        """
        Finds meshes with the name 'thumb' and calculates their half positions.
        Ensures each position is added only once.
        
        :rtype: list
        :return: List containing the unique half positions of all thumb joints.
        """
        # Find all meshes matching the thumb pattern
        meshes = self.find_meshes_with_name("*_L_thumb*")
        print(f"Thumb meshes found: {meshes}")
        
        p_list = []
        unique_positions = set()  # To store unique positions only
        
        # Iterate over each found mesh
        for mesh in meshes:
            print(f"Processing mesh: {mesh}")
            p = self.get_half_positions(mesh)
            print(f"Position for {mesh}: {p}")
            
            # Check if the position is unique
            if p not in unique_positions:
                p_list.append(p)
                unique_positions.add(p)  # Add to the set to prevent duplicates
        
        print(f"Final unique positions: {p_list}")
        p_tuple = tuple(p_list)
        return p_tuple


    def get_L_thumb1_joint_pos(self):
        p1, p2, p3 = self.get_L_thumb_joints_pos()
        print(f"p1: {p1}")
        print(p1)
        return p1
    def get_L_thumb2_joint_pos(self):
        p1, p2, p3 = self.get_L_thumb_joints_pos()
        print(f"p2: {p2}")
        return p2
    def get_L_thumb3_joint_pos(self):
        p1, p2, p3 = self.get_L_thumb_joints_pos()
        print(f"p3: {p3}")
        return p3


    def get_L_index_joints_pos(self):
        """
        Finds meshes with the name 'thumb' and calculates their half positions.
        Ensures each position is added only once.
        
        :rtype: list
        :return: List containing the unique half positions of all thumb joints.
        """
        # Find all meshes matching the thumb pattern
        meshes = self.find_meshes_with_name("*_L_index*")
        print(f"Thumb meshes found: {meshes}")
        
        p_list = []
        unique_positions = set()  # To store unique positions only
        
        # Iterate over each found mesh
        for mesh in meshes:
            print(f"Processing mesh: {mesh}")
            p = self.get_half_positions(mesh)
            print(f"Position for {mesh}: {p}")
            
            # Check if the position is unique
            if p not in unique_positions:
                p_list.append(p)
                unique_positions.add(p)  # Add to the set to prevent duplicates
        
        print(f"Final unique positions: {p_list}")
        p_tuple = tuple(p_list)
        return p_tuple
    
    def get_L_index1_joint_pos(self):
        p1, p2, p3 = self.get_L_index_joints_pos()
        return p1
    def get_L_index2_joint_pos(self):
        p1, p2, p3 = self.get_L_index_joints_pos()
        return p2
    def get_L_index3_joint_pos(self):
        p1, p2, p3 = self.get_L_index_joints_pos()
        return p3

    def get_L_pinky_joints_pos(self):
        """
        Finds meshes with the name 'thumb' and calculates their half positions.
        Ensures each position is added only once.
        
        :rtype: list
        :return: List containing the unique half positions of all thumb joints.
        """
        # Find all meshes matching the thumb pattern
        meshes = self.find_meshes_with_name("*_L_pinky*")
        print(f"Thumb meshes found: {meshes}")
        
        p_list = []
        unique_positions = set()  # To store unique positions only
        
        # Iterate over each found mesh
        for mesh in meshes:
            print(f"Processing mesh: {mesh}")
            p = self.get_half_positions(mesh)
            print(f"Position for {mesh}: {p}")
            
            # Check if the position is unique
            if p not in unique_positions:
                p_list.append(p)
                unique_positions.add(p)  # Add to the set to prevent duplicates
        
        print(f"Final unique positions: {p_list}")
        p_tuple = tuple(p_list)
        return p_tuple
    
    def get_L_pinky1_joint_pos(self):
        p1, p2, p3 = self.get_L_pinky_joints_pos()
        return p1
    def get_L_pinky2_joint_pos(self):
        p1, p2, p3 = self.get_L_pinky_joints_pos()
        return p2
    def get_L_pinky3_joint_pos(self):
        p1, p2, p3 = self.get_L_pinky_joints_pos()
        return p3  

    ####################################################################
    # legs
    def get_L_but_joint_pos(self):
        """
        Retrieves the position of the 'L_but' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_but' mesh
        """
        mesh = self.find_meshes_with_name("*_L_but*")
        p = self.get_half_positions(mesh)
        return p

    def get_L_knee_joint_pos(self):
        """
        Retrieves the position of the 'L_knee' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_knee' mesh
        """
        mesh = self.find_meshes_with_name("*_L_knee*")
        p = self.get_half_positions(mesh)
        return p

    def get_L_ankle_joint_pos(self):
        """
        Retrieves the position of the 'L_ankle' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_ankle' mesh
        """
        mesh = self.find_meshes_with_name("*_L_ankle*")
        p = self.get_half_positions(mesh)
        return p

    def get_L_foot_joint_pos(self):
        """
        Retrieves the position of the 'L_foot' mesh and calculates the bottom center minimum Z position.
        
        :rtype: tuple
        :return: Tuple representing the bottom minimum Z position of the 'L_foot' mesh
        """
        mesh = self.find_meshes_with_name("*_L_foot*")
        p = self.get_pos_bottom_minz_center(mesh)
        return p

    def get_L_toe_joint_pos(self):
        """
        Retrieves the position of the 'L_toe' mesh and calculates the bottom center maximum Z position.
        
        :rtype: tuple
        :return: Tuple representing the bottom maximum Z position of the 'L_toe' mesh
        """
        mesh = self.find_meshes_with_name("*_L_toe*")
        p = self.get_pos_bottom_maxz_center(mesh)
        return p
    
