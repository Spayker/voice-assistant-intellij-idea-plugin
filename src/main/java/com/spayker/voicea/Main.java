package com.spayker.voicea;

import com.intellij.openapi.actionSystem.*;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.ui.Messages;

/**
 *  A stub implementation of AnAction class.
 *  Last one represents an entity that has a state, a presentation and can be performed.
 **/
public class Main extends AnAction {

    public Main() {
        super("Hello");
    }

    /**
     *  Implements this method to provide custom action handler.
     *  @param event
     **/
    @Override
    public void actionPerformed(AnActionEvent event) {
        Project project = event.getProject();
        Messages.showMessageDialog(project, "Hello world!", "Greeting", Messages.getInformationIcon());
    }

}
