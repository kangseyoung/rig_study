import maya.cmds as cmds


class RigStudyClass:
    """
    A class for studying Maya rigging-related scripts.

    Methods:
    --------
    run_create_joint():
        Iterates through transform objects and creates hierarchical joints.

    create_hierarchical_joint(obj):
        Creates joints at the position of the given object and recursively creates joints for its children.

    get_center_pos(obj):
        Returns the center position of the given object based on its bounding box.

    bind_skin(joint_):
        Binds the given joint to the corresponding mesh if it exists.

    get_mesh(joint_):
        Retrieves the mesh name based on the joint name.
    """

    def run_create_joint(self):
        """
        Iterates through all transform nodes, excluding camera nodes,
        and calls the method to create hierarchical joints for each object.
        """
        except_nodes = ['front', 'persp', 'side', 'top']  # Excluded camera nodes
        objs = cmds.ls(type="transform")
        for obj in objs:
            if obj not in except_nodes:
                self.create_hierarchical_joint(obj)

    def create_hierarchical_joint(self, obj):
        """
        Creates a joint at the position of the given object. If the object has child transform nodes,
        joints are recursively created for the children as well.

        Parameters:
        -----------
        obj : str
            The name of the object to create joints for.
        """
        center_pos = self.get_center_pos(obj)

        # Create a joint at the current object's position
        obj_joint = cmds.joint(name=f"{obj}_joint", radius=0.5)

        # Try to bind the joint to a mesh, handle any errors if the mesh does not exist
        try:
            mesh = self.bind_skin(obj_joint)
        except Exception as e:
            print(f"Error during skin binding: {e}")

        # Move the joint to the center position or to the object position if no center position is found
        if not center_pos:
            pos = cmds.xform(obj, query=True, worldSpace=True, translation=True)
            cmds.move(pos[0], pos[1], pos[2], obj_joint)
        else:
            cmds.move(center_pos[0], center_pos[1], center_pos[2], obj_joint)

        # Recursively create joints for any child transform nodes
        children = cmds.listRelatives(obj, children=True, type="transform")
        print("Children: ", children)
        if not children:
            print("There are no children for this object.")
            return

        for child in children:
            cmds.select(f'{obj_joint}')
            self.create_hierarchical_joint(child)

    def get_center_pos(self, obj):
        """
        Retrieves the center position of the given object's bounding box.

        Parameters:
        -----------
        obj : str
            The name of the object to get the center position for.

        Returns:
        --------
        list or None:
            The center position [x, y, z] of the object if it has a shape node,
            or None if no shape node is found.
        """
        shape_node = cmds.listRelatives(obj, shapes=True, fullPath=True)
        if not shape_node:
            print("No shape nodes found for this object.")
            return None

        # Calculate the center of the bounding box
        bbox = cmds.exactWorldBoundingBox(shape_node)
        center_pos = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]
        return center_pos

    def bind_skin(self, joint_):
        """
        Binds the given joint to a corresponding mesh.

        Parameters:
        -----------
        joint_ : str
            The name of the joint to bind.

        Raises:
        -------
        ValueError:
            If the corresponding mesh does not exist.

        Returns:
        --------
        str or None:
            The name of the mesh if the binding is successful, or None if not.
        """
        mesh = self.get_mesh(joint_)
        print(mesh)
        if not cmds.objExists(mesh):
            raise ValueError(f"Mesh {mesh} not found.")

        # Create a skin cluster to bind the joint to the mesh
        skin_cluster = cmds.skinCluster(joint_, mesh, toSelectedBones=True)
        print(f"Skin binding completed: {skin_cluster}")
        return mesh

    def get_mesh(self, joint_):
        """
        Retrieves the mesh name based on the joint name.

        Parameters:
        -----------
        joint_ : str
            The name of the joint.

        Returns:
        --------
        str:
            The name of the corresponding mesh.
        """
        mesh_name = joint_.split("_joint")[0]
        cmds.objExists(mesh_name)
        return mesh_name

    def get_hierarchy_order(self, grp):
            """
            Returns the joint creation order based on the provided group type.
            """
            if grp == "*_body_Grp":

                order_list = ["*_spine1", 
                              "*_spine2", 
                              "*_chest", 
                              "*_neck", 
                              "*_head"]
                
            elif grp == "*_leg_Grp":

                order_list = ["*_but",
                               "*_Thighs", 
                               "*_knee",
                               "*_calf", 
                               "*_ankle", 
                               "*_foot", 
                               "*_toe"]
                
            elif grp == "*_arm_Grp":
                order_list = ["*_shoulder"
                              , "*_upper_arm"
                              , "*_elbow"
                              , "*_lower_arm"
                              , "*_wrist"
                              , "*_hand"]

            elif grp == "*_finger_Grp":
                # Finger joints added
                order_list = [
                    "*_thumb1", "*_thumb2", "*_thumb3",       # Thumb joints
                    "*_index1", "*_index2", "*_index3",       # Index finger joints
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
# Run the script
joint_maker = RigStudyClass()
joint_maker.run_create_joint()
