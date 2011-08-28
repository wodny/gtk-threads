#include <gtk/gtk.h>
#include <pthread.h>

struct args_s
{
    int *argc;
    char ***argv;
};

static void destroy( GtkWidget *widget,
                     gpointer   data )
{
    gtk_main_quit ();
}

void *second_thread (void *args_p)
{
    GtkWidget *window;
    GtkWidget *button;

    struct args_s *args = (struct args_s*)args_p;

    gdk_threads_enter ();

    gtk_init (args->argc, args->argv);
    
    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    
    g_signal_connect (window, "destroy",
		      G_CALLBACK (destroy), NULL);
    
    button = gtk_button_new_with_label ("Hello World");
    
    gtk_container_add (GTK_CONTAINER (window), button);
    gtk_widget_show (button);
    gtk_widget_show (window);

    gtk_main ();
    gdk_threads_leave ();
}

int main( int   argc,
          char *argv[] )
{
    g_thread_init (NULL);
    gdk_threads_init ();

    pthread_t thread;
    struct args_s args;
    args.argc = &argc;
    args.argv = &argv;
    
    pthread_create (&thread, NULL, second_thread, &args);
    pthread_join(thread, NULL);
    
    return 0;
}

/* vim: set sw=4: */
