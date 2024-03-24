export default function Comment({ comment, currentUserId, recipeId }) {
    const { data } = useQuery('currentUser', () => post('users'));
    const [editIsOpen, setEditIsOpen] = useState(false);
    const [deleteIsOpen, setDeleteIsOpen] = useState(false);


    const dateOptions = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
    }
    let comment = {};
    let recipeId = "";

    const name = comment.authorId?.display_name || "";
    const authorId = comment.authorId?._id || "";
    const commentId = comment?._id || "";
    const text = comment?.text || "";
    let date = comment?.createdAt
        ? new Date(comment.createdAt).toLocaleString('en-US', dateOptions)
        : "";
    const editIsOpen = true;
    const deleteIsOpen = false;

    return (

        { text }

        
        
            {
        data.user?._id === authorId &&
            (

                setEditIsOpen(true)} className = 'pink-btn' > Edit
    setDeleteIsOpen(true)
} className = 'pink-btn' > Delete
                                            
                )

            }

{ name }


-


    { date }

        
                    )