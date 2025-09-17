---
Dia: 2025-09-16
dg-publish: true
---

``` java 
package com.equo.chromium.utils.events;

/**
 * Abstract base class for all browser events.
 * Each concrete event type must implement getEventType() to identify its specific type.
 */
public abstract class BrowserEvent {
    /**
     * Returns the specific event type for this event instance.
     * @return the EventType corresponding to this event
     */
    public abstract EventType getEventType();
}

package com.equo.chromium.utils.events;

/**
 * Event fired when a frame finishes loading.
 * Contains information about the loaded frame including HTML content and frame hierarchy.
 */
public class LoadEndEvent extends BrowserEvent {
    private final boolean isMain;
    private final String html;
    private final String frameName;
    private final String frameId;
    private final String parentFrameId;
    
    /**
     * Creates a new LoadEndEvent.
     * @param isMain true if this is the main frame
     * @param html the HTML content of the loaded frame
     * @param frameName the name of the frame
     * @param frameId the unique identifier of the frame
     * @param parentFrameId the identifier of the parent frame, or "0" if none
     */
    public LoadEndEvent(boolean isMain, String html, String frameName, String frameId, String parentFrameId) {
        this.isMain = isMain;
        this.html = html;
        this.frameName = frameName;
        this.frameId = frameId;
        this.parentFrameId = parentFrameId;
    }
    
    /**
     * @return true if this is the main frame
     */
    public boolean isMain() { return isMain; }
    
    /**
     * @return the HTML content of the loaded frame
     */
    public String getHtml() { return html; }
    
    /**
     * @return the name of the frame
     */
    public String getFrameName() { return frameName; }
    
    /**
     * @return the unique identifier of the frame
     */
    public String getFrameId() { return frameId; }
    
    /**
     * @return the identifier of the parent frame, or "0" if this is a top-level frame
     */
    public String getParentFrameId() { return parentFrameId; }
    
    @Override
    public EventType getEventType() { return EventType.onLoadEnd; }
}

/**
 * Event fired when a load operation encounters an error.
 * Contains the error code associated with the failed load operation.
 */
public class LoadErrorEvent extends BrowserEvent {
    private final int errorCode;
    
    /**
     * Creates a new LoadErrorEvent.
     * @param errorCode the error code indicating the type of load failure
     */
    public LoadErrorEvent(int errorCode) {
        this.errorCode = errorCode;
    }
    
    /**
     * @return the error code indicating the type of load failure
     */
    public int getErrorCode() { return errorCode; }
    
    @Override
    public EventType getEventType() { return EventType.onLoadError; }
}

/**
 * Event fired when navigation has finished.
 * Contains error information if the navigation failed.
 */
public class NavigationFinishedEvent extends BrowserEvent {
    private final int errorCode;
    
    /**
     * Creates a new NavigationFinishedEvent.
     * @param errorCode the error code, or 0 if navigation was successful
     */
    public NavigationFinishedEvent(int errorCode) {
        this.errorCode = errorCode;
    }
    
    /**
     * @return the error code, or 0 if navigation was successful
     */
    public int getErrorCode() { return errorCode; }
    
    @Override
    public EventType getEventType() { return EventType.onNavigationFinished; }
}

/**
 * Event fired when a find operation completes.
 * Contains information about search results including match count and active match position.
 */
public class FindResultEvent extends BrowserEvent {
    private final int count;
    private final int activeMatchOrdinal;
    
    /**
     * Creates a new FindResultEvent.
     * @param count the total number of matches found
     * @param activeMatchOrdinal the ordinal position of the currently active match (1-based)
     */
    public FindResultEvent(int count, int activeMatchOrdinal) {
        this.count = count;
        this.activeMatchOrdinal = activeMatchOrdinal;
    }
    
    /**
     * @return the total number of matches found
     */
    public int getCount() { return count; }
    
    /**
     * @return the ordinal position of the currently active match (1-based)
     */
    public int getActiveMatchOrdinal() { return activeMatchOrdinal; }
    
    @Override
    public EventType getEventType() { return EventType.onFindResult; }
}

/**
 * Event fired when a console message is logged by the web page.
 * Contains the message details including severity level, content, source location, and line number.
 */
public class ConsoleMessageEvent extends BrowserEvent {
    private final String level;
    private final String message;
    private final String source;
    private final int line;
    
    /**
     * Creates a new ConsoleMessageEvent.
     * @param level the severity level of the message (e.g., "INFO", "WARN", "ERROR")
     * @param message the content of the console message
     * @param source the source file or URL where the message originated
     * @param line the line number in the source file
     */
    public ConsoleMessageEvent(String level, String message, String source, int line) {
        this.level = level;
        this.message = message;
        this.source = source;
        this.line = line;
    }
    
    /**
     * @return the severity level of the message (e.g., "INFO", "WARN", "ERROR")
     */
    public String getLevel() { return level; }
    
    /**
     * @return the content of the console message
     */
    public String getMessage() { return message; }
    
    /**
     * @return the source file or URL where the message originated
     */
    public String getSource() { return source; }
    
    /**
     * @return the line number in the source file
     */
    public int getLine() { return line; }
    
    @Override
    public EventType getEventType() { return EventType.onConsoleMessage; }
}

/**
 * Event fired after the browser instance has been created and is ready for use.
 * Contains a reference to the created browser instance.
 */
public class AfterCreatedEvent extends BrowserEvent {
    private final ChromiumBrowser browser;
    
    /**
     * Creates a new AfterCreatedEvent.
     * @param browser the ChromiumBrowser instance that was created
     */
    public AfterCreatedEvent(ChromiumBrowser browser) {
        this.browser = browser;
    }
    
    /**
     * @return the ChromiumBrowser instance that was created
     */
    public ChromiumBrowser getBrowser() { return browser; }
    
    @Override
    public EventType getEventType() { return EventType.onAfterCreated; }
}

/**
 * Generic event for simple notifications that don't carry additional data.
 * Used for events like onLoadStart, onZoomChanged, etc.
 */
public class SimpleEvent extends BrowserEvent {
    private final EventType eventType;
    
    /**
     * Creates a new SimpleEvent.
     * @param eventType the type of event this represents
     */
    public SimpleEvent(EventType eventType) {
        this.eventType = eventType;
    }
    
    @Override
    public EventType getEventType() { return eventType; }
}


package com.equo.chromium.utils.events;

/**
 * Functional interface for type-safe event listeners.
 * @param <T> the specific type of BrowserEvent this listener handles
 */
@FunctionalInterface
public interface BrowserEventListener<T extends BrowserEvent> {
    /**
     * Called when the subscribed event occurs.
     * @param event the event instance containing event-specific data
     */
    void onEvent(T event);
}


package com.equo.chromium.utils;

import com.equo.chromium.utils.events.*;
import java.util.function.Function;

/**
 * Abstract base class for event actions that can be executed in response to browser events.
 * Provides automatic type inference for return values based on the event type.
 * 
 * @param <T> the return type of the action, automatically inferred from the EventType
 */
public abstract class EventAction<T> implements Function<BrowserEvent, T> {
    private final EventType expectedEventType;
    private final Class<T> returnType;
    protected BrowserEvent event;
    
    /**
     * Creates a new EventAction with automatic return type inference.
     * The return type is automatically determined based on the EventType.
     * 
     * @param expectedEventType the type of event this action handles
     */
    @SuppressWarnings("unchecked")
    public EventAction(EventType expectedEventType) {
        this.expectedEventType = expectedEventType;
        this.returnType = (Class<T>) inferReturnType(expectedEventType);
        this.event = createDefaultEvent(expectedEventType);
    }
    
    /**
     * Infers the appropriate return type based on the event type.
     * This method defines the semantic mapping between events and their expected return types.
     * 
     * @param eventType the event type to infer the return type for
     * @return the Class object representing the inferred return type
     */
    private static Class<?> inferReturnType(EventType eventType) {
        switch (eventType) {
            case onLoadEnd:
            case onConsoleMessage:
            case onNavigationFinished:
                return Boolean.class;
            case onLoadError:
            case onClipboardWriteText:
            case onClipboardReadText:
            case onOpenFile:
            case onCancelOpenFile:
                return String.class;
            case onFindResult:
                return Integer.class;
            case onAfterCreated:
            case onLoadStart:
            case onLoadingStateChange:
            case onZoomChanged:
            case onFullScreenEntered:
            case onFullScreenExited:
            case onNavigationStart:
                return Void.class;
            default:
                return Object.class;
        }
    }
    
    /**
     * Creates a default event instance with placeholder values.
     * This allows immediate access to event fields during development.
     * 
     * @param eventType the type of event to create
     * @return a default instance of the appropriate event type
     */
    private BrowserEvent createDefaultEvent(EventType eventType) {
        switch (eventType) {
            case onLoadEnd:
                return new LoadEndEvent(false, "", "", "", "");
            case onLoadError:
                return new LoadErrorEvent(0);
            case onConsoleMessage:
                return new ConsoleMessageEvent("", "", "", 0);
            case onFindResult:
                return new FindResultEvent(0, 0);
            case onAfterCreated:
                return new AfterCreatedEvent(null);
            case onNavigationFinished:
                return new NavigationFinishedEvent(0);
            default:
                return new SimpleEvent(eventType);
        }
    }
    
    /**
     * @return the current event instance
     */
    public BrowserEvent getEvent() {
        return event;
    }
    
    /**
     * @return the event type this action is designed to handle
     */
    public EventType getExpectedEventType() {
        return expectedEventType;
    }
    
    /**
     * Applies this action to the given event and returns the result.
     * This method is called internally by the event system.
     * 
     * @param event the event that triggered this action
     * @return the result of executing the action
     */
    @Override
    public final T apply(BrowserEvent event) {
        this.event = event;
        return run();
    }
    
    /**
     * Executes the action logic for the current event.
     * Subclasses must implement this method to define their specific behavior.
     * 
     * @return the result of the action, with type automatically inferred from the EventType
     */
    public abstract T run();
}

/**
 * Specialized EventAction for load end events that returns Boolean values.
 * Provides direct access to LoadEndEvent data without casting.
 */
public abstract class LoadEndAction extends EventAction<Boolean> {
    /**
     * Creates a new LoadEndAction.
     */
    public LoadEndAction() {
        super(EventType.onLoadEnd);
    }
    
    /**
     * @return the LoadEndEvent instance for this action
     */
    protected LoadEndEvent getLoadEndEvent() {
        return (LoadEndEvent) event;
    }
}

/**
 * Specialized EventAction for console message events that returns Boolean values.
 * Provides direct access to ConsoleMessageEvent data without casting.
 */
public abstract class ConsoleMessageAction extends EventAction<Boolean> {
    /**
     * Creates a new ConsoleMessageAction.
     */
    public ConsoleMessageAction() {
        super(EventType.onConsoleMessage);
    }
    
    /**
     * @return the ConsoleMessageEvent instance for this action
     */
    protected ConsoleMessageEvent getConsoleMessageEvent() {
        return (ConsoleMessageEvent) event;
    }
}

/**
 * Specialized EventAction for load error events that returns String values.
 * Provides direct access to LoadErrorEvent data without casting.
 */
public abstract class LoadErrorAction extends EventAction<String> {
    /**
     * Creates a new LoadErrorAction.
     */
    public LoadErrorAction() {
        super(EventType.onLoadError);
    }
    
    /**
     * @return the LoadErrorEvent instance for this action
     */
    protected LoadErrorEvent getLoadErrorEvent() {
        return (LoadErrorEvent) event;
    }
}

/**
 * Specialized EventAction for find result events that returns Integer values.
 * Provides direct access to FindResultEvent data without casting.
 */
public abstract class FindResultAction extends EventAction<Integer> {
    /**
     * Creates a new FindResultAction.
     */
    public FindResultAction() {
        super(EventType.onFindResult);
    }
    
    /**
     * @return the FindResultEvent instance for this action
     */
    protected FindResultEvent getFindResultEvent() {
        return (FindResultEvent) event;
    }
}

/**
 * Specialized EventAction for after created events that returns Void.
 * Provides direct access to AfterCreatedEvent data without casting.
 */
public abstract class AfterCreatedAction extends EventAction<Void> {
    /**
     * Creates a new AfterCreatedAction.
     */
    public AfterCreatedAction() {
        super(EventType.onAfterCreated);
    }
    
    /**
     * @return the AfterCreatedEvent instance for this action
     */
    protected AfterCreatedEvent getAfterCreatedEvent() {
        return (AfterCreatedEvent) event;
    }
}

/**
 * Specialized EventAction for navigation finished events that returns Boolean values.
 * Provides direct access to NavigationFinishedEvent data without casting.
 */
public abstract class NavigationFinishedAction extends EventAction<Boolean> {
    /**
     * Creates a new NavigationFinishedAction.
     */
    public NavigationFinishedAction() {
        super(EventType.onNavigationFinished);
    }
    
    /**
     * @return the NavigationFinishedEvent instance for this action
     */
    protected NavigationFinishedEvent getNavigationFinishedEvent() {
        return (NavigationFinishedEvent) event;
    }
}

/**
 * Generic EventAction for simple events with customizable return type.
 * Used for events that don't have specialized action classes.
 * 
 * @param <T> the return type for this action
 */
public abstract class SimpleAction<T> extends EventAction<T> {
    /**
     * Creates a new SimpleAction with explicit return type.
     * 
     * @param eventType the event type this action handles
     * @param returnType the class representing the return type
     */
    public SimpleAction(EventType eventType, Class<T> returnType) {
        super(eventType);
    }
    
    /**
     * @return the SimpleEvent instance for this action
     */
    protected SimpleEvent getSimpleEvent() {
        return (SimpleEvent) event;
    }
}

// Listener wrapper class
package com.equo.chromium.utils;

import com.equo.chromium.utils.events.BrowserEvent;

/**
 * Wrapper class that associates an EventAction with its event type.
 * Handles the execution of EventAction instances when events are fired.
 */
public class BrowserEventActionListener {
    private final EventAction<?> action;
    
    /**
     * Creates a new listener that wraps the given EventAction.
     * 
     * @param action the EventAction to wrap and execute
     */
    public BrowserEventActionListener(EventAction<?> action) {
        this.action = action;
    }
    
    /**
     * @return the event type this listener is subscribed to
     */
    public EventType getEventType() {
        return action.getExpectedEventType();
    }
    
    /**
     * @return the wrapped EventAction instance
     */
    public EventAction<?> getAction() {
        return action;
    }
    
    /**
     * Handles the execution of the wrapped EventAction when an event is fired.
     * 
     * @param event the event that triggered this listener
     * @return the result returned by the EventAction's run() method
     */
    public Object handleEvent(BrowserEvent event) {
        return action.apply(event);
    }
}


```

step 1: lgrar que si yo pongo un return o que la funcion retorne y yo pueda agarrar el independent browser y en vez de retornar false poder retornar la ejecucion de la funcion que el cliente pueda llegar a ejecutar.

hacer las modioficaciones necesarias para que subscriber.notifysubscribers devuelva lo que devuelva la funcion.

segundo stP: cambiar la url de navegacion. Agarramos y hacelos el geturl de request y lo cambiamos con load