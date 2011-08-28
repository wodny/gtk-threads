#include <gtk/gtk.h>
#include <pthread.h>

static void destroy( GtkWidget *widget,
                     gpointer   data )
{
    gtk_main_quit ();
}

void *second_thread (void *args)
{
    gdk_threads_enter ();
    gtk_main ();
    gdk_threads_leave ();
}

int main( int   argc,
          char *argv[] )
{
    GtkWidget *window;
    GtkWidget *button;

    g_thread_init (NULL);
    gdk_threads_init ();
    gdk_threads_enter ();

    gtk_init (&argc, &argv);
    
    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    
    g_signal_connect (window, "destroy",
		      G_CALLBACK (destroy), NULL);
    
    button = gtk_button_new_with_label ("Hello World");
    
    gtk_container_add (GTK_CONTAINER (window), button);
    gtk_widget_show (button);
    gtk_widget_show (window);

    gdk_threads_leave ();

    pthread_t thread;
    
    pthread_create (&thread, NULL, second_thread, NULL);
    pthread_join(thread, NULL);
    
    return 0;
}

/* vim: set sw=4: */
