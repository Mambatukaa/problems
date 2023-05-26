package LeetCode.Tree;

import java.util.ArrayList;

public class TreeN{
    String data;
    ArrayList<TreeN> children;

    public TreeN(String data) {
        this.data = data;
        this.children = new ArrayList<TreeN>();
    }


    public void addChild(TreeN node) {
        this.children.add(node);

    }

    public String print(int level) {
        StringBuilder ret;
        ret = new StringBuilder(" ".repeat(level) + data + "\n");

        for (TreeN node : this.children) {
            ret.append(node.print(level + 1));
        }

        return ret.toString();
    }


}
