/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSF/JSFManagedBean.java to edit this template
 */
package learning.jee.simpleee6app.presentation;

import java.io.Serializable;
import javax.ejb.EJB;
import javax.inject.Named;
import javax.enterprise.context.Dependent;
import learning.jee.simpleee6app.boundary.MessageFacade;
import learning.jee.simpleee6app.entity.Message;

/**
 *
 * @author Quintin.Henn
 */
@Named(value = "messageView")
@Dependent
public class MessageView implements Serializable {
    
    // Injects the MessageFacade session bean using the @EJB annotation
    @EJB
    private MessageFacade messageFacade;
    
    private Message message;

    /**
     * Creates a new instance of MessageView
     */
    public MessageView() {
        this.message = new Message();
    }
    
    // Calls getMessage to retrieve the message
    public Message getMessage() {
       return message;
    }

    // Returns the total number of messages
    public int getNumberOfMessages(){
       return messageFacade.findAll().size();
    }

    // Saves the message and then returns the string "theend"
    public String postMessage(){
       this.messageFacade.create(message);
       return "theend";
    }
}
