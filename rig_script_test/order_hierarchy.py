import maya.cmds as cmds

class MakeHierarchy:
    """
    Creates a hierarchical structure of joints including fingers.
    """

    def get_hierarchy_order(self, grp):
        """
        Returns the joint creation order based on the provided group type.
        """
        if grp == "*_body_Grp":
            order_list = ["*_spine1", "*_spine2", "*_chest", "*_neck", "*_head"]
            
        elif grp == "*_leg_Grp":
            order_list = ["*_but", "*_Thighs", "*_knee", "*_calf", "*_ankle", "*_foot", "*_toe"]
            
        elif grp == "*_arm_Grp":
            order_list = ["*_shoulder", "*_upper_arm", "*_elbow", "*_lower_arm", "*_wrist", "*_hand"]

        elif grp == "*_finger_Grp":
            # Finger joints added
            order_list = [
                "*_thumb1", "*_thumb2", "*_thumb3",       # Thumb joints
                "*_index1", "*_index2", "*_index3",       # Index finger joints
                "*_middle1", "*_middle2", "*_middle3",    # Middle finger joints
                "*_ring1", "*_ring2", "*_ring3",          # Ring finger joints
                "*_pinky1", "*_pinky2", "*_pinky3"        # Pinky finger joints
            ]
        
        else:
            order_list = []  # Default empty list if the group is not recognized

        return order_list

    def create_joint_hierarchy(self, grp, prefix):
        """
        Creates the joint hierarchy based on the group type and the prefix provided.
        
        Parameters:
        -----------
        grp : str
            The group type (e.g., '*_body_Grp', '*_leg_Grp', '*_arm_Grp', '*_finger_Grp').
        prefix : str
            The prefix to be used for naming the joints (e.g., 'BonyWalker').
        """
        # Get the hierarchy order for the given group
        order_list = self.get_hierarchy_order(grp)

        if not order_list:
            print(f"No valid hierarchy found for group: {grp}")
            return

        # Create the joints in the correct hierarchical order
        for part in order_list:
            joint_name = part.replace(prefix,'*') + "_joint"  # Replace '*' with the prefix for each part
            cmds.joint(name=joint_name)  # Create joint with the generated name
            print(f"Joint created: {joint_name}")

        print("Joint hierarchy created successfully!")
    
# Create an instance of the MakeHierarchy class
rig_maker = MakeHierarchy()

# Example: Create a body hierarchy for a character with the prefix "BonyWalker"
rig_maker.create_joint_hierarchy("*_body_Grp", "BonyWalker")