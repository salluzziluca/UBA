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


package com.equo.chromium.internal;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;

import org.cef.CefSettings.LogSeverity;
import org.cef.browser.CefBrowser;
import org.cef.browser.CefFrame;
import org.cef.callback.CefStringVisitor;

import com.equo.chromium.ChromiumBrowser;
import com.equo.chromium.utils.EventAction;
import com.equo.chromium.utils.EventType;
import com.equo.chromium.utils.BrowserEventActionListener;
import com.equo.chromium.utils.events.*;

/**
 * Manages event subscriptions and notifications for browser events.
 * Supports both EventAction-based subscriptions and functional interface subscriptions.
 */
public class Subscriber {
    private IndependentBrowser _browser;
    private Map<EventType, List<BrowserEventActionListener>> actionListeners = new HashMap<>();
    private Map<EventType, List<BrowserEventListener<? extends BrowserEvent>>> typedListeners = new HashMap<>();
    private Map<Long, ActionData> subscribeIndex = new HashMap<>();
    private long eventId = 0;
    private boolean firstLoading = true;
    private int _errorCode = 0;
    protected static EventAction eventActionOfAfterCreated = null;

    /**
     * Internal class to track subscription data for cleanup purposes.
     */
    class ActionData {
        public EventType eventType;
        public BrowserEventActionListener actionListener;
        public BrowserEventListener<? extends BrowserEvent> typedListener;

        /**
         * Creates ActionData for an EventAction-based subscription.
         */
        public ActionData(EventType eventType, BrowserEventActionListener actionListener) {
            this.eventType = eventType;
            this.actionListener = actionListener;
        }
        
        /**
         * Creates ActionData for a functional interface subscription.
         */
        public ActionData(EventType eventType, BrowserEventListener<? extends BrowserEvent> typedListener) {
            this.eventType = eventType;
            this.typedListener = typedListener;
        }
    }

    /**
     * Creates a new Subscriber for the given browser instance.
     * 
     * @param browser the browser instance to manage events for
     */
    public Subscriber(IndependentBrowser browser) {
        _browser = browser;
    }

    /**
     * Disposes of this subscriber and cleans up all subscriptions.
     */
    public void dispose() {
        _browser = null;
        unSubscribeAll();
    }

    /**
     * Sets a global EventAction to be executed when any browser is created.
     * This is a legacy method for backward compatibility.
     * 
     * @param eventAction the action to execute on browser creation
     */
    public static void subscribeOnAfterCreated(EventAction eventAction) {
        eventActionOfAfterCreated = eventAction;
    }

    /**
     * @return the global after-created EventAction, if any
     */
    public static EventAction getEventActionOfAfterCreated() {
        return eventActionOfAfterCreated;
    }

    /**
     * Subscribes an EventAction to be executed when events of its expected type occur.
     * The EventAction determines its own event type and return type automatically.
     * 
     * @param <T> the return type of the EventAction
     * @param action the EventAction to subscribe
     * @return a unique identifier for this subscription, used for unsubscribing
     */
    public synchronized <T> long subscribe(EventAction<T> action) {
        EventType eventType = action.getExpectedEventType();
        BrowserEventActionListener listener = new BrowserEventActionListener(action);
        _browser.isCreated().thenRun(() -> {
            actionListeners.computeIfAbsent(eventType, m -> new ArrayList<>()).add(listener);
            subscribeIndex.put(eventId, new ActionData(eventType, listener));
        });
        return eventId++;
    }

    /**
     * Subscribes a functional interface listener for the specified event type.
     * 
     * @param <T> the specific BrowserEvent subtype
     * @param eventType the type of event to subscribe to
     * @param listener the functional interface to call when events occur
     * @return a unique identifier for this subscription, used for unsubscribing
     */
    public synchronized <T extends BrowserEvent> long subscribe(EventType eventType, BrowserEventListener<T> listener) {
        _browser.isCreated().thenRun(() -> {
            typedListeners.computeIfAbsent(eventType, m -> new ArrayList<>()).add(listener);
            subscribeIndex.put(eventId, new ActionData(eventType, listener));
        });
        return eventId++;
    }

    /**
     * Convenience method to subscribe to load end events.
     * 
     * @param listener the listener to call when frames finish loading
     * @return subscription identifier
     */
    public long subscribeToLoadEnd(BrowserEventListener<LoadEndEvent> listener) {
        return subscribe(EventType.onLoadEnd, listener);
    }

    /**
     * Convenience method to subscribe to load error events.
     * 
     * @param listener the listener to call when load errors occur
     * @return subscription identifier
     */
    public long subscribeToLoadError(BrowserEventListener<LoadErrorEvent> listener) {
        return subscribe(EventType.onLoadError, listener);
    }

    /**
     * Convenience method to subscribe to console message events.
     * 
     * @param listener the listener to call when console messages are logged
     * @return subscription identifier
     */
    public long subscribeToConsoleMessage(BrowserEventListener<ConsoleMessageEvent> listener) {
        return subscribe(EventType.onConsoleMessage, listener);
    }

    /**
     * Convenience method to subscribe to find result events.
     * 
     * @param listener the listener to call when find operations complete
     * @return subscription identifier
     */
    public long subscribeToFindResult(BrowserEventListener<FindResultEvent> listener) {
        return subscribe(EventType.onFindResult, listener);
    }

    /**
     * Convenience method to subscribe to after created events.
     * 
     * @param listener the listener to call when the browser is created
     * @return subscription identifier
     */
    public long subscribeToAfterCreated(BrowserEventListener<AfterCreatedEvent> listener) {
        return subscribe(EventType.onAfterCreated, listener);
    }

    /**
     * Convenience method to subscribe to navigation finished events.
     * 
     * @param listener the listener to call when navigation completes
     * @return subscription identifier
     */
    public long subscribeToNavigationFinished(BrowserEventListener<NavigationFinishedEvent> listener) {
        return subscribe(EventType.onNavigationFinished, listener);
    }

    /**
     * Unsubscribes a previously registered event listener.
     * 
     * @param idEvent the subscription identifier returned by a subscribe method
     * @return true if the subscription was found and removed
     */
    public synchronized boolean unSubscribe(long idEvent) {
        _browser.isCreated().thenRun(() -> {
            ActionData actionData = subscribeIndex.get(idEvent);
            if (actionData != null) {
                if (actionData.actionListener != null) {
                    actionListeners.get(actionData.eventType).remove(actionData.actionListener);
                }
                if (actionData.typedListener != null) {
                    typedListeners.get(actionData.eventType).remove(actionData.typedListener);
                }
                subscribeIndex.remove(idEvent);
            }
        });
        return true;
    }

    /**
     * Removes all subscriptions managed by this Subscriber.
     */
    public synchronized void unSubscribeAll() {
        subscribeIndex.clear();
        actionListeners.clear();
        typedListeners.clear();
    }

    /**
     * Notifies all subscribers of the specified event type with the given event data.
     * Executes all matching EventActions and functional interface listeners asynchronously.
     * 
     * @param eventType the type of event that occurred
     * @param event the event data to pass to subscribers
     */
    @SuppressWarnings("unchecked")
    protected synchronized void notifySubscribers(EventType eventType, BrowserEvent event) {
        actionListeners.computeIfAbsent(eventType, m -> new ArrayList<>()).forEach(listener -> {
            CompletableFuture.runAsync(() -> {
                Object result = listener.handleEvent(event);
            });
        });

        typedListeners.computeIfAbsent(eventType, m -> new ArrayList<>()).forEach(listener -> {
            CompletableFuture.runAsync(() -> {
                try {
                    ((BrowserEventListener<BrowserEvent>) listener).onEvent(event);
                } catch (ClassCastException ex) {
                    System.err.println("Type mismatch in event listener for " + eventType + ": " + ex.getMessage());
                }
            });
        });
    }

    /**
     * Handles browser creation events from the browser.
     * 
     * @param browser the browser instance that was created
     */
    public void onAfterCreatedNotify(CefBrowser browser) {
        ChromiumBrowser chromiumBrowser = (ChromiumBrowser) browser.getReference();
        AfterCreatedEvent event = new AfterCreatedEvent(chromiumBrowser);
        
        if (eventActionOfAfterCreated != null && !_browser.isCreated().isDone()) {
            Object result = eventActionOfAfterCreated.apply(event);
        }
        _browser.isCreated().complete(true);
        notifySubscribers(EventType.onAfterCreated, event);
    }

    /**
     * Handles frame load completion events from the browser.
     * 
     * @param frame the browser frame that finished loading
     */
    public void onLoadEndNotify(CefFrame frame) {
        CefFrame parentFrame = frame.getParent();
        final boolean isMain = frame.isMain();
        final String parentId = parentFrame != null ? parentFrame.getIdentifier() : "0";
        
        frame.getSource(new CefStringVisitor() {
            @Override
            public void visit(String source) {
                String jsonSource = source.replaceAll("\"", "\\\\\"").replaceAll("\n", "\\\\n");
                LoadEndEvent event = new LoadEndEvent(isMain, jsonSource, frame.getName(), 
                                                     frame.getIdentifier(), parentId);
                notifySubscribers(EventType.onLoadEnd, event);
            }
        });
    }

    /**
     * Handles loading state change events from the browser.
     * 
     * @param isLoading true if the browser is currently loading
     * @param url the URL being loaded
     */
    public void onLoadingStateChangeNotify(boolean isLoading, String url) {
        if (firstLoading || isLoading) {
            notifySubscribers(EventType.onLoadingStateChange, new SimpleEvent(EventType.onLoadingStateChange));
            firstLoading = false;
        } else {
            firstLoading = true;
        }
    }

    /**
     * Handles navigation start events from the browser.
     */
    public void onBeforeBrowseNotify() {
        notifySubscribers(EventType.onNavigationStart, new SimpleEvent(EventType.onNavigationStart));
    }

    /**
     * Handles address change events from the browser, indicating navigation completion.
     * 
     * @param isLoading true if the browser is still loading
     * @param url the new URL
     */
    public void onAddressChangeNotify(boolean isLoading, String url) {
        NavigationFinishedEvent event = new NavigationFinishedEvent(_errorCode);
        _errorCode = 0;
        notifySubscribers(EventType.onNavigationFinished, event);
    }

    /**
     * Handles load error events from the browser.
     * 
     * @param error the error code indicating the type of load failure
     */
    public void onLoadErrorNotify(int error) {
        LoadErrorEvent event = new LoadErrorEvent(error);
        _errorCode = error;
        notifySubscribers(EventType.onLoadError, event);
    }

    /**
     * Handles load start events from the browser.
     */
    public void onLoadStartNotify() {
        notifySubscribers(EventType.onLoadStart, new SimpleEvent(EventType.onLoadStart));
    }

    /**
     * Handles find result events from the browser.
     * 
     * @param count the total number of matches found
     * @param activeMatchOrdinal the position of the currently active match
     */
    public void onFindResultNotify(int count, int activeMatchOrdinal) {
        FindResultEvent event = new FindResultEvent(count, activeMatchOrdinal);
        notifySubscribers(EventType.onFindResult, event);
    }

    /**
     * Handles console message events from the browser.
     * 
     * @param level the severity level of the message
     * @param message the content of the console message
     * @param source the source file or URL where the message originated
     * @param line the line number in the source file
     */
    public void onConsoleMessageNotify(LogSeverity level, String message, String source, int line) {
        ConsoleMessageEvent event = new ConsoleMessageEvent(level.toString(), message, source, line);
        notifySubscribers(EventType.onConsoleMessage, event);
    }

    /**
     * Handles fullscreen mode change events from the browser.
     * 
     * @param fullscreen true if entering fullscreen mode, false if exiting
     */
    public void onFullscreenModeChangeNotify(boolean fullscreen) {
        EventType eventType = fullscreen ? EventType.onFullScreenEntered : EventType.onFull
```

step 1: lgrar que si yo pongo un return o que la funcion retorne y yo pueda agarrar el independent browser y en vez de retornar false poder retornar la ejecucion de la funcion que el cliente pueda llegar a ejecutar.

hacer las modioficaciones necesarias para que subscriber.notifysubscribers devuelva lo que devuelva la funcion.

segundo stP: cambiar la url de navegacion. Agarramos y hacelos el geturl de request y lo cambiamos con load



```py 
def recieve_selective_repeat(args, download_socket, filesize):

""" Implementación del protocolo Selective Repeat para la recepción de archivos

Ventana deslizante con tamaño fijo, manejo de ACKs individuales y reenvío de paquetes perdidos.

La función asume que los paquetes tienen el formato "seq_num:chunk" y que el servidor envía

los paquetes en orden secuencial, pero pueden llegar fuera de orden o perderse.

La función también maneja la creación del archivo de destino, ya sea en un directorio o con un nombre específico.

La función utiliza un diccionario para almacenar los paquetes recibidos y sus tiempos de recepción,

permitiendo reintentos para paquetes que no se confirman dentro de un tiempo límite.

  

explicacion paso a paso:

1. Se determina la ruta completa del archivo de destino, ya sea en un director

2. Se abre el archivo en modo escritura binaria.

3. Se inicializan variables para la ventana deslizante, el número base,

4. Se inicia un bucle que continúa hasta que se hayan recibido todos los bytes del archivo.

5. Dentro del bucle, se intenta recibir un paquete del servidor.

6. Se extrae el número de secuencia y el contenido del paquete.

7. Se verifica si el número de secuencia está dentro de la ventana actual.

- Si es así, se escribe el contenido en el archivo y se envía un ACK

- Si no, se ignora el paquete y, si es un paquete antiguo, se reenvía el ACK correspondiente.

8. Se maneja el caso de timeout y paquetes malformados.

9. Finalmente, se cierra el archivo y se confirma la descarga exitosa.

"""

if os.path.isdir(args.dst):

file_path = os.path.join(args.dst, args.name)

else:

file_path = args.dst

print(f"Saving file to: {file_path}")

with open(file_path, "wb") as file:

window_size = 4 #cant_pkt_env / 2 -> #cant_pkt_env = file_size / channel_size

base_num = 0

bytes_sent = 0

pkts = {} # Diccionario: {seq_num: (packet, sent_time)}

while bytes_sent < filesize:

try:

packet, _ = download_socket.recvfrom(4096)

seq_str, chunk = packet.split(b":", 1)

seq_received = int(seq_str)

if base_num <= seq_received < base_num + window_size:

if seq_received not in pkts:

file.write(chunk)

bytes_sent += len(chunk)

pkts[seq_received] = (packet, None)

print(f"Received and wrote packet {seq_received}.")

download_socket.sendto(f"ACK:{seq_received}".encode(), (args.host, args.port))

print(f"Sent ACK for packet {seq_received}.")

while base_num in pkts:

del pkts[base_num]

base_num += 1

else:

print(f"Received out-of-window packet {seq_received}, expected window [{base_num}, {base_num + window_size - 1}]. Ignoring.")

if seq_received < base_num:

download_socket.sendto(f"ACK:{seq_received}".encode(), (args.host, args.port))

print(f"Resent ACK for old packet {seq_received}.")

except socket.timeout:

print("Timeout waiting for packet. The server might have stopped.")

break

except ValueError:

print("Received a malformed packet. Ignoring.")




def send_selective_repeat(self, client_socket, addr, file_path):
        try:

            client_socket.settimeout(TIMEOUT)

            filesize = os.path.getsize(file_path)
            success = True

            with open(file_path, "rb") as file:
                base = 0
                next_seq_num = 0
                window_size = 4
                buffer = {}
                bytes_sent = 0

                while bytes_sent < filesize or buffer:
                    while next_seq_num < base + window_size and bytes_sent < filesize:
                        chunk = file.read(1024)
                        if not chunk:
                            break
                        
                        packet = f"{next_seq_num}:".encode() + chunk
                        client_socket.sendto(packet, addr)
                        buffer[next_seq_num] = chunk
                        next_seq_num += 1
                        bytes_sent += len(chunk)

                    try:
                        data, _ = client_socket.recvfrom(1024)
                        response = data.decode()
                        if response.startswith("ACK:"):
                            ack_num = int(response.split(":")[1])
                            if ack_num in buffer:
                                del buffer[ack_num]
                                if ack_num == base:
                                    while base not in buffer and base < next_seq_num:
                                        base += 1
                    except socket.timeout:
                        print("Timeout waiting for ACKs, resending unacknowledged packets...")
                        for seq in range(base, next_seq_num):
                            if seq in buffer:
                                packet = f"{seq}:".encode() + buffer[seq]
                                client_socket.sendto(packet, addr)

                client_socket.sendto(b"EOF", addr)

            return success

        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            success = False
            return success
```