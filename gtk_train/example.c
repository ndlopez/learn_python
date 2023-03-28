#include <gtk/gtk.h>
static void print_hallo(GtkWidget *widget,gpointer data){
    g_print("halllo word\n");
}
static void activate(GtkApplication* app,gpointer user_data){
    GtkWidget *window;
    window=gtk_application_window_new(app);
    GtkWidget *button=gtk_application_new_with_label("hallo work");
    gtk_window_set_title(GTK_WINDOW(window),"My Window");
    gtk_window_set_default_size(GTK_WINDOW(window),200,200);
    //gtk_widget_show(window);
    //gtk_widget_show(button);
    g_signal_connect(button,"clicked",G_CALLBACK(print_hallo),NULL);
    gtk_window_set_child(GTK_WINDOW(window),button);
    gtk_window_present(GTK_WINDOW(window));
}

int main(int argc,char **argv){
    GtkApplication *app;
    int status;
    app=gtk_application_new("org.gtk.example",G_APPLICATION_FLAGS_NONE);
    g_signal_connect(app,"activate",G_CALLBACK(activate),NULL);
    status=gtk_application_run(G_APPLICATION(app),argc,argv);
    g_object_unref(app);
    return status;
}