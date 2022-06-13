from lab1.model.GeometryPrimitives.Point import Point


class Branch:
    def __init__(self, data: Point, left_child: 'Branch' = None, right_child: 'Branch' = None):
        self.__data = data
        self.__left_child = left_child
        self.__right_child = right_child

    @property
    def data(self) -> Point:
        return self.__data

    @property
    def left_child(self) -> 'Branch':
        return self.__left_child

    @property
    def right_child(self) -> 'Branch':
        return self.__right_child

    @left_child.setter
    def left_child(self, branch: 'Branch'):
        self.__left_child = branch

    @right_child.setter
    def right_child(self, branch: 'Branch'):
        self.__right_child = branch

    def __str__(self):
        return f"Branch: Point({self.data.x}, {self.data.y}, distance = {self.data.distance_from_origin:.2f})"


class BinaryTree:
    def __init__(self, root: Branch = None):
        self.__root = root

    def add_element(self, element: Branch, start_branch: Branch = None) -> None:
        if self.__root is None:
            self.__root = element
            return

        current_pos = self.__root if start_branch is None else start_branch
        while True:
            if element.data.distance_from_origin >= current_pos.data.distance_from_origin:    ###
                if current_pos.right_child is not None:
                    current_pos = current_pos.right_child
                else:
                    current_pos.right_child = element
                    break
            else:
                if current_pos.left_child is not None:
                    current_pos = current_pos.left_child
                else:
                    current_pos.left_child = element
                    break

    def __find_element_by_point(self, root: Branch, p: Point) -> Branch:
        if root is None:
            return None
        if root.data.distance_from_origin == p.distance_from_origin:
            return root
        elif root.data.distance_from_origin <= p.distance_from_origin:    ###
            return self.__find_element_by_point(root.right_child, p)
        else:
            return self.__find_element_by_point(root.left_child, p)

    def find_element_by_point(self, p: Point) -> Branch:
        return self.__find_element_by_point(self.__root, p)

    def __print_all_branches(self, branch: Branch, depth: int) -> None:
        if branch is None:
            print("\t-".expandtabs(2 * depth))
            return
        print(("\t" + str(branch)).expandtabs(2 * depth))
        self.__print_all_branches(branch.left_child, depth + 1)
        self.__print_all_branches(branch.right_child, depth + 1)

    def print_all_branches(self) -> None:
        self.__print_all_branches(self.__root, 0)

    def __print_all_branches_positive_y(self, branch: Branch, depth: int) -> None:
        if branch is None:
            print("\t-".expandtabs(2 * depth))
            return
        if branch.data.y > 0:
            print(("\t" + str(branch)).expandtabs(2 * depth))
        else:
            print("\t-".expandtabs(2 * depth))
        self.__print_all_branches(branch.left_child, depth + 1)
        self.__print_all_branches(branch.right_child, depth + 1)

    def print_all_branches_positive_y(self) -> None:
        self.__print_all_branches_positive_y(self.__root, 0)

    def delete_branch(self, branch: Branch) -> None:
        if self.__root is None:
            return
        if self.__root == branch:
            self.__root = None
            return
        current_branch = self.__root
        while True:
            if current_branch.data.distance_from_origin <= branch.data.distance_from_origin:    ###
                if current_branch.right_child == branch:
                    if branch.right_child is None and branch.left_child is None:
                        current_branch.right_child = None
                    elif branch.right_child is not None:
                        current_branch.right_child = branch.right_child
                        if branch.left_child is not None:
                            self.add_element(branch.left_child, current_branch)
                    else:
                        current_branch.right_child = branch.left_child
                    return
                if current_branch.right_child is None:
                    return
                current_branch = current_branch.right_child
            else:
                if current_branch.left_child == branch:
                    if branch.right_child is None and branch.left_child is None:
                        current_branch.left_child = None
                    elif branch.right_child is not None:
                        current_branch.left_child = branch.right_child
                        if branch.left_child is not None:
                            self.add_element(branch.left_child, current_branch)
                    else:
                        current_branch.left_child = branch.left_child
                    return
                if current_branch.left_child is None:
                    return
                current_branch = current_branch.left_child

    def destroy(self) -> None:
        self.__root = None

    def __check_branch(self, branch: Branch) -> None:
        if branch is None:
            return
        self.__check_branch(branch.left_child)
        if branch.data.x < 0 and branch.data.y < 0:
            self.delete_branch(branch)
        self.__check_branch(branch.right_child)
        if branch.data.x < 0 and branch.data.y < 0:
            self.delete_branch(branch)

    def delete_branches_negative_xy(self) -> None:
        self.__check_branch(self.__root)
