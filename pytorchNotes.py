'''
Save model and reload to continue training
'''
# save model
save_checkpoint({
    'epoch': epoch + 1,
    'arch': args.arch,
    'state_dict': model.state_dict(),
    'best_prec1': best_prec1,
    'optimizer' : optimizer.state_dict(),
}, is_best)

#reload
if args.resume:
    if os.path.isfile(args.resume):
        print("=> loading checkpoint '{}'".format(args.resume))
        checkpoint = torch.load(args.resume)
        args.start_epoch = checkpoint['epoch']
        best_prec1 = checkpoint['best_prec1']
        model.load_state_dict(checkpoint['state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer'])
        print("=> loaded checkpoint '{}' (epoch {})"
              .format(args.resume, checkpoint['epoch']))
